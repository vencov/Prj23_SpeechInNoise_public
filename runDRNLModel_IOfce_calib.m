% Script for runing the GT model connected with OME filter
%


folder = fileparts(which(mfilename));   % find .m file folder
addpath(genpath(folder));               % add path to all subfolders

fs = 44.1e3;
tx = (0:1/fs:100e-3).';
ftone = 1000;
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


Lref = 96; % assume that each file is at 96dB SPL
Levels = 0:2:120;
for lev = 1:length(Levels)
    
    [COME_r, Spast_r] = initOMEpar( fs );      % initialisation function of the OME parameters
    [CBM_r, pastVal_r ] = initDRNLBMpar( 300, fs );% initialisation function of the BM parameters
    %[CIHC_r, pastValIHC_r ] = initIHCpar( fs, 1e3 );% initialisation function of the BM parameters
    
    
    
    Ltest = Levels(lev);
    
    
    scaleTone = 10^((Ltest-Lref)/20);
    
    
    %     sig_in = scaleRec*rec + scaleSum*sum(1:length(rec));  % speech + noise
    
    %     Lset = Levels(lev)
    
    sig_in = sig_in/sqrt(mean(sig_in.^2));
    sig_in_r = 1e-17*scaleTone*sig_in;
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
        [sigOutBM_r, pastVal_r] = fce_BMdrnl(sigOutOME_r, CBM_r, pastVal_r);
        %[sigOutIHC_r, pastValIHC_r ] = fce_IHC_Dau(sigOutBM_r, CIHC_r, pastValIHC_r);
        sigOutOMEWav = [sigOutOMEWav sigOutOME_r];
        sigOutBMWav = [sigOutBMWav; sigOutBM_r.']; % To see the intern representation
        %sigOutIHCWav = [sigOutIHCWav; sigOutIHC_r]; % To see the intern representation
        %sigOutIHC_r(sigOutIHC_r<1.6e-3) = 1.6e-3; % global thresholding
        %sigOutLog_r = 20*log10(sigOutIHC_r/1.6e-3);    % logarithmic scale
        %sigOutLogWav = [sigOutLogWav; sigOutLog_r];
    end
    if lev==1
        [~,idxMax] = max(sqrt(mean(sigOutBMWav.^2)));
    end
    
    out(lev) = sqrt(mean(sigOutBMWav(:,idxMax).^2));
    
end

%save final results for all signals
%outOME_GT{i} = sigOutOMEWav;
%outBM_GT{i} = sigOutBMWav;
%outIHC_GT{i} = sigOutIHCWav;
