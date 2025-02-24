function [ BMdisp_buf2, pastVal ] = fce_BMNobili(sigOutOME, CBM, fs, pastVal )
%Function which simulate the Basilar Membrane part of the cochlear model
%   input arguments   
%        - sigOutOME : Signal to process through the basilar Membrane
%        - CBM : Structure which contain all parameters usefull for all the
%        calculs
%        - fs : sampling frequency
%        - pastVal : Past values for the second derivation 
% 
%   Output arguments 
%        - BMdisp_buf2 : Output signal after processing througt BM Part
%        - pastVal : Update of past values for the second derivation of the next
%        buffer


%% BM Part
nTimes = CBM.upsample; % Number of upsampling 

sigOutOME = [pastVal.dummyXX;sigOutOME']; % Concatenation to have the previons values of past input
L=length(sigOutOME);                      % Length of then concatenated imput signal 

inpA=(sigOutOME(3:L)+sigOutOME(1:L-2)-2*sigOutOME(2:L-1)); % Second d�rivation
inpB = [pastVal.inpAPast;inpA];  % Concatenation to have the previons values for the interpolation

pastVal.inpAPast = inpA(end);    % Update of the last value of the signal to use in the next buffer

%% Definition of vectors for the interpolation :
tx=0:1/fs:(length(inpB)-1)/fs;  
txUp=0:1/(nTimes*fs):(nTimes*length(inpB)-nTimes)/(nTimes*fs);

%% interpolation
inp_buf = interp1(tx', inpB, txUp'); % Interpolation to increase values of the input signal between tx and txUp 
inp_buf = inp_buf(2:end);

%% Update of the dummyXX value for the next buffer
pastVal.dummyXX = sigOutOME(end-1:end); % Update of the two last values of the imput signal to use in the next buffer

% L=length(inp_buf);
    X = pastVal.X;
    W = pastVal.W;
    Y = pastVal.Y;
    dT =  CBM.dT;
    Da = CBM.Da;
    Dy = CBM.Dy;
    Dw = CBM.Dw;
    Vs = CBM.Vs;
    Mh = CBM.Mh;
    dV =pastVal.dV;
    V = pastVal.V;
    nl_adjust = CBM.nl_adjust;
    DampSp = CBM.DampSp;
    undamp = CBM.undamp;
    stiff = CBM.stiff;
    nsect = CBM.nsect;
    BMdisp_buf = zeros(length(inp_buf),nsect); 
    %BMdisp_buf = zeros(length(tx)-1,nsect);

for t=1:length(inp_buf)
      
            % --------- TM equations -------------------
            dW = -Dw.*W - Dy.*Y - Da.*dV; % +0.1*input(t);%TM acceleration times dT, last term = 
      										%driving force neg. proportional to BM acc.							
      
            Y  = Y + W*dT;  % TM displacement incrementation
            W  = W + dW*dT; % TM velocity incrementation 
            
            Ycut = nonlin(Y,nl_adjust); % Vetesnik

            dV = -Vs*inp_buf(t) - Mh* (stiff.*X + DampSp*V + 1*undamp.*Ycut);
         
                               % BM acceleration times dT
                               % Mh (mexican hats) = inverse of Green's fun. matrix
                               % stiff = BM stiffness
                               % DampSp = BM damping due to absolute and shear
                               % organ of Corti viscosity (sparse matrix)
                               % undamp = it is shapeplot(tx,BMvel(:,100),'r--')d so as to compensate for DampSp
            X = X + V*dT;     % BM displacement incrementation
            V = V + dV*dT;    % BM velocity incrementation      
            BMdisp_buf(t,:) = X;  
end


    BMdisp_buf2 = BMdisp_buf(1:nTimes:end,:);
     pastVal.X = X;
     pastVal.W = W;
     pastVal.Y = Y;
     pastVal.dV=dV;
     pastVal.V = V;

end 

function [Z]=nonlin(Y,nl_adjust)
% nonlinear function taken from Vetesnik
     
Y  = 1.0*Y;     
y1=0.01139;
y2=0.03736;
c1=0.7293;
c2=1.4974;
b=0.30991;

Z=(1./(1+c1*exp(-nl_adjust.*Y./y1)+c2*exp(-nl_adjust.*Y./y2)+0.0))-b;

Z=0.1*Z./nl_adjust;
end





