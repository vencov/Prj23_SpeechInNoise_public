% script which calcualtes modulation index for the responses to sentences
%
%


Gcontrol  = 1; % to control model gain (1 - higher gain, 0.9 - lower gain)

% close all
clear all;
clc

folder = fileparts(which(mfilename));   % find .m file folder
addpath(genpath(folder));               % add path to all subfolders

load Sounds/SpeechInNoise/'babble noise.zvk' -mat   % nacte babble noise

noise = double(podnet{1})/2^16;
% noise = noise./sqrt(mean(noise.^2));
strret = {'01','02','03','04','05','06','07','08','09','10'};
% sqrt(mean(rec.^2))
Lcomp = 24; % compensation of RMS difference between RMS = 1 for 96 dB
fs = 44.1e3;
mezera = zeros(7*fs,1);

for sada=1:length(strret)
    
    load(['Sounds/SpeechInNoise/Sada_' strret{sada} '.zvk'],'-mat');   % nacte prvni sadu, promenna podnet{} ma bunky jednotlive promluvy
    sigL = mezera;
    N1 = length(mezera);
    idxB = [];
    for pk=1:length(podnet)
        idxB = [idxB; [N1+1,N1+length(podnet{pk})]];
        N1 = N1+length(podnet{pk})+length(mezera);
        sigL = [sigL; double(podnet{pk})/2^16; mezera];
        
        rec = double(podnet{pk})/2^16;
%         rec = rec./sqrt(mean(rec.^2));
%         xc(sada,pk) = sqrt(mean(rec.^2))
    end
    pomer = ceil(length(sigL) / length(noise));
    noiseall = repmat(noise,pomer,1);
    noiseall = noiseall(1:length(sigL));
    

    %
%    load(['Sounds\SpeechInNoise\Sada_' strret{sada} '.zvk'],'-mat');   % nacte prvni sadu, promenna podnet{} ma bunky jednotlive promluvy
    % for ss = 1:length(9)
    
    % load(['Sounds\SpeechInNoise\'Sada 02.zvk' -mat   % nacte prvni sadu, promenna podnet{} ma bunky jednotlive promluvy
    Levels = 30:5:90;
    XCm = zeros(length(Levels),length(podnet));
    XCq = zeros(length(Levels),length(podnet));
    for pk=1:length(podnet)
        
        rec = double(podnet{pk})/2^16;
%         rec = rec./sqrt(mean(rec.^2));
    %    xc(sada,pk) = sqrt(mean(rec.^2))
    

        Lref = 96; % assume that each file is at 96dB SPL
        
        
        for lk = 1:length(Levels)
%             
            Ltest = Levels(lk);
            SNR = -5;
%             
            scaleRec = 10^((Ltest-Lref+Lcomp)/20);
            scaleSum = 10^((Ltest-SNR-Lref+Lcomp)/20);
%             
%             sig_in = scaleRec*rec + scaleSum*noise(1:length(rec));  %
%             speech + noise 
            sig_in = scaleRec*rec + scaleSum*noiseall(idxB(pk,1):idxB(pk,2));  % s + noise for time idx in measurement
            sig_in_r = scaleRec*rec; % only speech
            fs = 44.1e3;
            %figure;
            %plot(sig_in)
            num_comp = 2;
            tlen = 0.02;
            tlen = 0.2;
            bufSize = round(tlen*fs);
            for i = 1:1%num_sig
                
                [COME_r, Spast_r] = initOMEpar( fs );      % initialisation function of the OME parameters
                [CBM_r, pastVal_r ] = initBMpar( 300, fs, Gcontrol );% initialisation function of the BM parameters
                [CIHC_r, pastValIHC_r ] = initIHCpar( fs, 1e3 );% initialisation function of the BM parameters
                
                %Lref = 94;                  % reference level for +-1 ampl.
                %Lset_r = Lref + 20*log10(sqrt(mean(yresamp{1+(i-1)*num_comp}.^2))*sqrt(2));
                %sig_in_r = 2e-5*10^(Lset_r/20)*yresamp{1+(i-1)*num_comp};
                nbBuf_ref=floor(length(sig_in_r)/bufSize); % Define the number of buffers
                
                
                nbBufA = nbBuf_ref;
                
                
                
                for k=1 : nbBufA
                    [sigOutOME_r, Spast_r] = fce_OME(sig_in_r(1+(k-1)*bufSize:k*bufSize)', COME_r, Spast_r);
                    [sigOutBM_r, pastVal_r] = fce_BMNobili(sigOutOME_r, CBM_r, fs, pastVal_r);
%                     [sigOutIHC_r, pastValIHC_r ] = fce_IHC_Dau(sigOutBM_r, CIHC_r, pastValIHC_r);
%                     sigOutIHC_r(sigOutIHC_r<1.6e-3) = 1.6e-3;
%                     sigOutLog_r = 20*log10(sigOutIHC_r/1.6e-3);
                    env = abs(hilbert(sigOutBM_r));
                    
                    mDW{lk}(k,:) = (sqrt(mean((env-mean(env)).^2)))./(mean(env));
                   
                    %sigOutOMEWav = [sigOutOMEWav sigOutOME];
                    %sigOutBMWav = [sigOutBMWav; sigOutBM]; % To see the intern representation
                    %sigOutIHCWav = [sigOutIHCWav; sigOutIHC]; % To see the intern representation
                end
            end
            %     hold on;
            %     plot(rm_coef);
            %   XC(lk,pk) = (mean(out_rm_c{1}(200,:)))
%             XC(lk,pk) = quantile(rm_coef,0.05)
            
        end
        
        
    end
    
    save(['Results/speechnoiseCalibB/pokusMIw200ms_sada' strret{sada} 'g10.mat'],'Levels','mDW')
    
end
% Folderres = 'Results/Coresv01/';
% save([Folderres 'out_rmNobili100ms.mat'],'out_rm_c','sig_all');
