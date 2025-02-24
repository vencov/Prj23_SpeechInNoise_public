% Script for runing the GT model connected with OME filter
%


folder = fileparts(which(mfilename));   % find .m file folder
addpath(genpath(folder));               % add path to all subfolders
fs = 44.1e3;

Lref = 96; % assume that each file is at 96dB SPL
Levels = [20 40 60 80]
CF = 4000
for lev = 1:length(Levels)
    
    %[CIHC_r, pastValIHC_r ] = initIHCpar( fs, 1e3 );% initialisation function of the BM parameters
    fvect = round(linspace(CF/3,CF*1.5,100),-1);
    fvect = [CF fvect]
    for fr = 1:length(fvect)
        
        [COME_r, Spast_r] = initOMEpar( fs );      % initialisation function of the OME parameters
        [CBM_r, pastVal_r ] = initBMpar( 300, fs );% initialisation function of the BM parameters
        
        Tdur = 160e-3;
        tx = (0:1/fs:Tdur).';
        ftone = fvect(fr);
        sig = sin(2*pi*ftone*tx);
        
        Rdur = 10e-3;
        x = [0:1/fs:Rdur]';
        x = pi*x/Rdur;
        rampUp = (1 + cos(x + pi))/2;
        
        rampDown = flipud(rampUp);
        
        wholeramp = [rampUp; ones(length(sig)-2*length(rampDown),1); rampDown];
        sig_in = wholeramp.*sig;
        
        
        tlen = 0.01;
        bufSize = round(tlen*fs);
        
        
        
        Ltest = Levels(lev);
        
        
        scaleTone = 10^((Ltest-Lref)/20);
        
        
        %     sig_in = scaleRec*rec + scaleSum*sum(1:length(rec));  % speech + noise
        
        %     Lset = Levels(lev)
        
        sig_in = sig_in/sqrt(mean(sig_in.^2));
        sig_in_r = scaleTone*sig_in;
        % Lset_r = Lref + 20*log10(sqrt(mean(sig_in.^2))*sqrt(2));
        
        % sig_in_r = 2e-5*10^(Lset_r/20)*sig_in;
        nbBuf=floor(length(sig_in_r)/bufSize); % Define the number of buffers
        
        sigOutBMWav = [];                       % initialisation of the output matrix in the for cicle
        sigOutOMEWav = [];                       % initialisation of the output matrix in the for cicle
        sigOutIHCWav = [];                       % initialisation of the output matrix in the for cicle
        sigOutLogWav = [];
        rm_coef = zeros(nbBuf,1);
        for k=1 : nbBuf
            [sigOutOME_r, Spast_r] = fce_OME(sig_in_r(1+(k-1)*bufSize:k*bufSize)', COME_r, Spast_r);
            [sigOutBM_r, pastVal_r] = fce_BMNobili(sigOutOME_r, CBM_r, fs, pastVal_r);
            %[sigOutIHC_r, pastValIHC_r ] = fce_IHC_Dau(sigOutBM_r, CIHC_r, pastValIHC_r);
            sigOutOMEWav = [sigOutOMEWav sigOutOME_r];
            sigOutBMWav = [sigOutBMWav; sigOutBM_r]; % To see the intern representation
            %sigOutIHCWav = [sigOutIHCWav; sigOutIHC_r]; % To see the intern representation
            %sigOutIHC_r(sigOutIHC_r<1.6e-3) = 1.6e-3; % global thresholding
            %sigOutLog_r = 20*log10(sigOutIHC_r/1.6e-3);    % logarithmic scale
            %sigOutLogWav = [sigOutLogWav; sigOutLog_r];
        end
        if fr==1
            [~,idxMax] = max(sqrt(mean(sigOutBMWav.^2)));
        end
        No = 2e3;
        Nwin = 4410;
        fx = (0:Nwin-1)*fs/Nwin; % frequency axis
        idxFt = find(fvect(fr)==fx);
        BMspect = fft(sigOutBMWav(No:No+Nwin-1,idxMax)).*exp(-sqrt(-1)*2*pi*fvect(fr)*No*1/fs);
        MEspect = fft(sigOutOMEWav(No:No+Nwin-1)).*exp(-sqrt(-1)*2*pi*fvect(fr)*No*1/fs);
        bmresp(fr) = BMspect(idxFt);
        meresp(fr) = MEspect(idxFt);
        
    end
    
%     save(['isointg10Lv' num2str(Ltest) 'dB' num2str(CF) 'Hz.mat'],'fvect','bmresp','meresp','Ltest');
    save(['isointg9Lv' num2str(Ltest) 'dB' num2str(CF) 'Hz.mat'],'fvect','bmresp','meresp','Ltest');
end

%save final results for all signals
%outOME_GT{i} = sigOutOMEWav;
%outBM_GT{i} = sigOutBMWav;
%outIHC_GT{i} = sigOutIHCWav;
