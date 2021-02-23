# AGRG-CIDCO
In order to use the script have a DEM of the area of interest available.
By default the script calculates the partial derivatives needed to create the geomorphometric variables.
The variables themselves are calculated in the ArcGIS raster calculator using the following equations (assuming you use the same naming convention I used).
If a different naming convention is used change the specific names of the variables while leaving the structure the same.

Plan Curvature
OutRas = -( Power("Variables\qVariable.tif",2)*"Variables\rVariable.tif"-2.0*"Variables\pVariable.tif"* "Variables\qVariable.tif"*"Variables\sVariable.tif"+ Power("Variables\pVariable.tif",2)*"Variables\tVariable.tif")/(Power(Power(Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3),0.5))

Horizontal Curvature
OutRas = -(Power("Variables\qVariable.tif",2)*"Variables\rVariable.tif"-2.0*"Variables\pVariable.tif"* "Variables\qVariable.tif"*"Variables\sVariable.tif"+ Power("Variables\pVariable.tif",2)*"Variables\tVariable.tif")/((Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2))*Power(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),0.5))

Vertical Curvature
OutRas = -(Power("Variables\pVariable.tif",2)*"Variables\rVariable.tif"-2.0*"Variables\pVariable.tif"* "Variables\qVariable.tif"*"Variables\sVariable.tif"+ Power("Variables\qVariable.tif",2)*"Variables\tVariable.tif")/((Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2))*Power( Power(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3),0.5))

Difference Curvature
OutRas = 0.5*("Geomorphometric\VerticalCurve.tif"-"Geomorphometric\HorizontalCurve4.tif")

Mean Curvature
OutRas = -( ((1+Power("Variables\qVariable.tif",2))*"Variables\rVariable.tif"-2*"Variables\pVariable.tif"*"Variables\qVariable.tif"*"Variables\sVariable.tif"+(1+Power("Variables\pVariable.tif",2))*"Variables\tVariable.tif") / (2*Power(Power(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3),0.5)) )

Unsphericity Curvature
OutRas =  Power((1/(4*Power(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3)))*(Power("Variables\rVariable.tif"*Power((1+Power("Variables\qVariable.tif",2)/1+Power("Variables\pVariable.tif",2)),0.5)-"Variables\tVariable.tif"*Power((1+Power("Variables\pVariable.tif",2)/1+Power("Variables\qVariable.tif",2)),0.5),2)*(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2))+Power("Variables\pVariable.tif"*"Variables\qVariable.tif"*"Variables\rVariable.tif"*Power((1+Power("Variables\qVariable.tif",2)/1+Power("Variables\pVariable.tif",2)),0.5)-2*"Variables\sVariable.tif"*Power((1+Power("Variables\qVariable.tif",2))*(1+Power("Variables\pVariable.tif",2)),0.5)+"Variables\pVariable.tif"*"Variables\qVariable.tif"*"Variables\tVariable.tif"*Power(1+Power("Variables\pVariable.tif",2)/1+Power("Variables\qVariable.tif",2),0.5),2)),0.5)

minimum curvature
OutRas = "MeanCurve.tif" - "UnsphericityCurve.tif"

Horizontal Excess Curvature
OutRas = "HorizontalCurve.tif" - "MinimumCurve.tif"

Vertical Excess Curvature
OutRas = "VerticalCurve.tif" - minimum curvature

Accumulation Curvature
OutRas =  "Geomorphometric\VerticalCurve.tif"*"Geomorphometric\HorizontalCurve.tif"

Ring Curvature
OutRas =  "HorizontalExcessCurve.tif"*"VerticalExcessCurve.tif"

Rotor
OutRas = (( Power("Variables\pVariable.tif",2)- Power("Variables\qVariable.tif",2)  )* "Variables\sVariable.tif"- "Variables\pVariable.tif"* "Variables\qVariable.tif"*("Variables\rVariable.tif"-"Variables\tVariable.tif"))/ Power( Power(( Power("Variables\pVariable.tif",2)+ Power("Variables\qVariable.tif",2) ),3) ,0.5)

Horizontal Curvature Deflection
OutRas = ( Power("Variables\qVariable.tif",3)*"Variables\gVariable.tif"-Power("Variables\pVariable.tif",3)*"Variables\hVariable.tif"+3*"Variables\pVariable.tif"*"Variables\qVariable.tif"*("Variables\pVariable.tif"*"Variables\mVariable.tif"-"Variables\qVariable.tif"*"Variables\kVariable.tif") )/( Power( Power( Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3)*(1+ Power("Variables\pVariable.tif",2)+ Power("Variables\qVariable.tif",2)),0.5) )-( "Geomorphometric\HorizontalCurve4.tif"*"Geomorphometric\rotor3"*(2+3*(Power("Variables\qVariable.tif",2)+ Power("Variables\qVariable.tif",2))/(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2)  ) ) )

Vertical Curvature Deflection
OutRas =  (  Power("Variables\qVariable.tif",3)*"Variables\mVariable.tif"-Power("Variables\pVariable.tif",3)*"Variables\kVariable.tif"+2*"Variables\pVariable.tif"*"Variables\qVariable.tif"*("Variables\qVariable.tif"*"Variables\kVariable.tif"-"Variables\pVariable.tif"*"Variables\mVariable.tif")-"Variables\pVariable.tif"*"Variables\qVariable.tif"*("Variables\qVariable.tif"*"Variables\hVariable.tif"-"Variables\pVariable.tif"*"Variables\gVariable.tif") ) / ( Power( Power( Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3)*(1+ Power("Variables\pVariable.tif",2)+ Power("Variables\qVariable.tif",2)),0.5) ) - ( "rotor"*(2*("Variables\rVariable.tif"+"Variables\tVariable.tif")/Power( Power(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2),3),0.5)+("VerticalCurve.tif"*(2+5*(Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2)))/(1+Power("Variables\pVariable.tif",2)+Power("Variables\qVariable.tif",2)))))

