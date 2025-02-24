function [ CBM, pastVal ] = initBMpar( nsect, fs, A )
%Function which calculates and initialize all parameters useful for the
%Basilar membrane part 
%
%   Input arguments
%         - nsect : Number of section (oscilators)
%         - fs : Sampling frequency
%         
%   Output arguments   
%         - CBM : Structure which contain all parameters useful for the Bm
%         part
%         - pastVal : Structure used to save the previous values for the calculation 
   

CBM.nsect = 300;
CBM.fmin = 200;
CBM.active = 1;
CBM.upsample = 10;
CBM.minSection = 210;
CBM.maxSection= 210;
CBM.scaleIN_N = 4;
fsup = CBM.upsample*fs;

[Mh, DampSp, stiff, Vs, x, dT, Da, Dy, Dw, bigamma, undamp, bmw] = alldataNL(nsect,1/fsup);
CBM.Mh = Mh;
CBM.DampSp = DampSp;
CBM.stiff = stiff;
CBM.Vs = Vs;
CBM.x = x;
CBM.dT = dT;
CBM.Da = Da;
CBM.Dy = Dy;
CBM.Dw = Dw;
CBM.bigamma = bigamma;
CBM.undamp = A*undamp;
CBM.bmw = bmw;
CBM.bufSize=2024; 
CBM.nl_adjust = ones(nsect,1);

pastVal.X = zeros(nsect,1);
pastVal.W = zeros(nsect,1);
pastVal.Y = zeros(nsect,1);
pastVal.dV= zeros(nsect,1);
pastVal.V = zeros(nsect,1);

pastVal.dummyXX = [0;0];    % initialisation of the matrix to save the two last values of previous input signal (for the derivation in fce_BM) 
pastVal.inpAPast = 0;       
  

end

