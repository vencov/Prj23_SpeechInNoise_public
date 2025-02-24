function [ sigOutOME, Spast] = fce_OME(yIn, COME, Spast)
%Function which simulate the processing of a song through the Outter-Middle Ear
%   input arguments   
%        - yIn : Signal to process
%        - COME : Structure which contain all parameters of filters
%        - Spast : Past values for calculation of filters
% 
%   Output arguments 
%        - SigOutOME : Output signal after processing througt OME Part
%        - Spast : Past values for calculation of future values of filters

scaleC = 1e17; 

[X1, Spast.S1] = filter(COME.bOE1, COME.aOE1, yIn, Spast.S1); 
[X2, Spast.S2] = filter(COME.bOE2, COME.aOE2, yIn, Spast.S2);
XInput2 = yIn + X1 + X2;
[X3, Spast.S3] = filter(COME.bME1, COME.aME1, XInput2, Spast.S3); 
[X0, Spast.S4] = filter(COME.bME2, COME.aME2, X3, Spast.S4);
 sigOutOME = (X0*COME.gME)*scaleC;

end