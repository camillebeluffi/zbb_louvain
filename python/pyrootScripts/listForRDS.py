import os, sys
lib_path = os.path.abspath('../')
sys.path.append(lib_path)

MuCorrFact = 1.0
Extra_norm={ "MuMuChannelDATA"  : 1.0,
             "EEChannelDATA"    : 1.0,
             "MuMuChannelTT"    : 1.0,#(2984./4412.)/MuCorrFact,
             "EEChannelTT"      : 1.0,
             "MuMuChannelTT-FullLept"    : (15000./62506.)/MuCorrFact,
             "EEChannelTT-SemiLept"      : 1.0,
             "MuMuChannelTT-SemiLept"    : 1.0,
             "EEChannelTT-FullLept"      : 15000./46492.,
	     "MuMuChannelZbb_Zbb"    : (20000./111784.)/MuCorrFact,
             "EEChannelZbb_Zbb"      : 20000./80672.,
	     "MuMuChannelZbb"    : 1.0/MuCorrFact,
             "EEChannelZbb"      : 1.0,
	     "MuMuChannelZbx"    : 1.0/MuCorrFact,
             "EEChannelZbx"      : 1.0,
	     "MuMuChannelZxx"    : 1.0/MuCorrFact,
             "EEChannelZxx"      : 1.0,
	     "MuMuChannelZno"    : 1.0/MuCorrFact,
             "EEChannelZno"      : 1.0,
	     "MuMuChannelZZ"    : (10000./16986.)/MuCorrFact,
             "EEChannelZZ"      : 10000./11936.,
	     "MuMuChannelZH125" : (10000./65412.)/MuCorrFact,
             "EEChannelZH125"   : 10000./48726.,

	     "MuMuChannelZH110" : (10000./58765.)/MuCorrFact,
             "EEChannelZH110"   : 10000./42745.,
	     "MuMuChannelZH115" : (10000./61456.)/MuCorrFact,
             "EEChannelZH115"   : 10000./44633.,
	     "MuMuChannelZH120" : (10000./63643.)/MuCorrFact,
             "EEChannelZH120"   : 10000./46265.,
	     "MuMuChannelZH130" : (10000./68489.)/MuCorrFact,
             "EEChannelZH130"   : 10000./50189.,
	     "MuMuChannelZH135" : (10000./69881.)/MuCorrFact,
             "EEChannelZH135"   : 10000./51567.,
	     "MuMuChannelZH140" : (10000./70994.)/MuCorrFact,
             "EEChannelZH140"   : 10000./52219.,
	     "MuMuChannelZH145" : (10000./73747.)/MuCorrFact,
             "EEChannelZH145"   : 10000./54375.,
	     "MuMuChannelZH150" : (10000./75391.)/MuCorrFact,
             "EEChannelZH150"   : 10000./56013.,

             "MuMuChannelDY50-70" : 1.,#4000./6517.,
             "EEChannelDY50-70" : 1.,#4000./4615.,
             "MuMuChannelDY70-100" : 1.,#2000./3242.,
             "EEChannelDY70-100" : 1.,#2000./2304.,
             "MuMuChannelDY100" : 1.,#5000./9040,
             "EEChannelDY100" : 1.,#5000./6789.,
             "MuMuChannelDY180" : 1.,#5000./7281.,
             "EEChannelDY180" : 1.,#5000./5648.,
             "MuMuChannelDY1j" : 5000./8655.,
             "EEChannelDY1j" : 5000./5942.,
             "MuMuChannelDY2j" : 15000./38485.,
             "EEChannelDY2j" : 15000./27727.,
             "MuMuChannelDY3j" : 15000./39129.,
             "EEChannelDY3j" : 15000./28325.,
             "MuMuChannelDY4j" : 25000./43536.,
             "EEChannelDY4j" : 25000./32339.,
            }

L_DY = 10325.26
DYlumi = {
    "DY50-70"   : 40626.58,
    "DY70-100"  : 27019.59,
    "DY100"     : 78068.53,
    "DY180"     : 341113.16,
    "DY1j"      : 41506.68,
    "DY2j"      : 119183.18,
    "DY3j"      : 203041.98,
    "DY4j"      : 277900.48,
    }

DYrew={}
for sample in DYlumi:
    for c in ["MuMuChannel","EEChannel"]:
        if sample!="DY180":
            DYrew[c+sample+"Extra_norm"]=str(L_DY/(DYlumi[sample]*Extra_norm[c+sample]+L_DY))
            DYrew[c+sample]=str(L_DY/(DYlumi[sample]+L_DY))
        else :
            DYrew[c+sample+"Extra_norm"]=str(L_DY/(DYlumi[sample]*Extra_norm[c+sample]+DYlumi["DY100"]*Extra_norm[c+"DY100"]+L_DY))
            DYrew[c+sample]=str(L_DY/(DYlumi[sample]+DYlumi["DY100"]+L_DY))            


#MM SFs

SFs_fit_MM = {}
SFs_fit_MM[""]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.94",
          "EEChannelTT"      : "*0.94",
          "MuMuChannelTT-FullLept"    : "*0.94",
          "EEChannelTT-FullLept"      : "*0.94",
          "MuMuChannelTT-SemiLept"    : "*0.94",
          "EEChannelTT-SemiLept"      : "*0.94",
          "MuMuChannelZbb"    : "*( (1.12*(@4==2))+(1.27*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.12*(@4==2))+(1.27*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.27",
          "EEChannelZbx"      : "*1.27",
          "MuMuChannelZxx"    : "*1.08",
          "EEChannelZxx"      : "*1.08",
          "MuMuChannelZno"    : "*1.08",
          "EEChannelZno"      : "*1.08",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

##########################test different SFs#################################
#SFs_fit_MM[""]={ "MuMuChannelDATA"  : "*1.0",
#          "EEChannelDATA"    : "*1.0",
#          "MuMuChannelTT"    : "*0.94",
#          "EEChannelTT"      : "*0.94",
#          "MuMuChannelTT-FullLept"    : "*0.94",
#          "EEChannelTT-FullLept"      : "*0.94",
#          "MuMuChannelTT-SemiLept"    : "*0.94",
#          "EEChannelTT-SemiLept"      : "*0.94",
#          "MuMuChannelZbb"    : "*( (1.08*(@4==2))+(1.22*(@4>2)) )",
#          "EEChannelZbb"      : "*( (1.08*(@4==2))+(1.22*(@4>2)) )",
#          "MuMuChannelZbx"    : "*1.80",
#          "EEChannelZbx"      : "*1.80",
#          "MuMuChannelZxx"    : "*0.99",
#          "EEChannelZxx"      : "*0.99",
#          "MuMuChannelZno"    : "*0.99",
#          "EEChannelZno"      : "*0.99",
#          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
#          "EEChannelZZ"      : "*(8.4/7.7)",
#          "MuMuChannelZH125" : "*1.0",
#          "EEChannelZH125"   : "*1.0",
#          "MuMuChannelZH115" : "*1.0",
#          "EEChannelZH115"   : "*1.0",
#          "MuMuChannelZH120" : "*1.0",
#          "EEChannelZH120"   : "*1.0",
#          "MuMuChannelZH130" : "*1.0",
#          "EEChannelZH130"   : "*1.0",
#          "MuMuChannelZH135" : "*1.0",
#          "EEChannelZH135"   : "*1.0",
#          }
#########################################################################

SFs_fit_MM["_bcBTAGup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.90",
          "EEChannelTT"      : "*0.90",
          "MuMuChannelTT-FullLept"    : "*0.90",
          "EEChannelTT-FullLept"      : "*0.90",
          "MuMuChannelTT-SemiLept"    : "*0.90",
          "EEChannelTT-SemiLept"      : "*0.90",
          "MuMuChannelZbb"    : "*( (1.07*(@4==2))+(1.21*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.07*(@4==2))+(1.21*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.21",
          "EEChannelZbx"      : "*1.21",
          "MuMuChannelZxx"    : "*1.03",
          "EEChannelZxx"      : "*1.03",
          "MuMuChannelZno"    : "*1.03",
          "EEChannelZno"      : "*1.03",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_bcBTAGdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.98",
          "EEChannelTT"      : "*0.98",
          "MuMuChannelTT-FullLept"    : "*0.98",
          "EEChannelTT-FullLept"      : "*0.98",
          "MuMuChannelTT-SemiLept"    : "*0.98",
          "EEChannelTT-SemiLept"      : "*0.98",
          "MuMuChannelZbb"    : "*( (1.18*(@4==2))+(1.33*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.18*(@4==2))+(1.33*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.33",
          "EEChannelZbx"      : "*1.33",
          "MuMuChannelZxx"    : "*1.14",
          "EEChannelZxx"      : "*1.14",
          "MuMuChannelZno"    : "*1.14",
          "EEChannelZno"      : "*1.14",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_lBTAGup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.94",
          "EEChannelTT"      : "*0.94",
          "MuMuChannelTT-FullLept"    : "*0.94",
          "EEChannelTT-FullLept"      : "*0.94",
          "MuMuChannelTT-SemiLept"    : "*0.94",
          "EEChannelTT-SemiLept"      : "*0.94",
          "MuMuChannelZbb"    : "*( (1.12*(@4==2))+(1.26*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.12*(@4==2))+(1.26*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.26",
          "EEChannelZbx"      : "*1.26",
          "MuMuChannelZxx"    : "*0.96",
          "EEChannelZxx"      : "*0.96",
          "MuMuChannelZno"    : "*0.96",
          "EEChannelZno"      : "*0.96",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_lBTAGdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.94",
          "EEChannelTT"      : "*0.94",
          "MuMuChannelTT-FullLept"    : "*0.94",
          "EEChannelTT-FullLept"      : "*0.94",
          "MuMuChannelTT-SemiLept"    : "*0.94",
          "EEChannelTT-SemiLept"      : "*0.94",
          "MuMuChannelZbb"    : "*( (1.13*(@4==2))+(1.28*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.13*(@4==2))+(1.28*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.28",
          "EEChannelZbx"      : "*1.28",
          "MuMuChannelZxx"    : "*1.22",
          "EEChannelZxx"      : "*1.22",
          "MuMuChannelZno"    : "*1.22",
          "EEChannelZno"      : "*1.22",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_JERup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.95",
          "EEChannelTT"      : "*0.95",
          "MuMuChannelTT-FullLept"    : "*0.95",
          "EEChannelTT-FullLept"      : "*0.95",
          "MuMuChannelTT-SemiLept"    : "*0.95",
          "EEChannelTT-SemiLept"      : "*0.95",
          "MuMuChannelZbb"    : "*( (1.23*(@4==2))+(1.24*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.23*(@4==2))+(1.24*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.24",
          "EEChannelZbx"      : "*1.24",
          "MuMuChannelZxx"    : "*0.97",
          "EEChannelZxx"      : "*0.97",
          "MuMuChannelZno"    : "*0.97",
          "EEChannelZno"      : "*0.97",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_JESup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.94",
          "EEChannelTT"      : "*0.94",
          "MuMuChannelTT-FullLept"    : "*0.94",
          "EEChannelTT-FullLept"      : "*0.94",
          "MuMuChannelTT-SemiLept"    : "*0.94",
          "EEChannelTT-SemiLept"      : "*0.94",
          "MuMuChannelZbb"    : "*( (1.14*(@4==2))+(1.16*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.14*(@4==2))+(1.16*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.16",
          "EEChannelZbx"      : "*1.16",
          "MuMuChannelZxx"    : "*1.04",
          "EEChannelZxx"      : "*1.04",
          "MuMuChannelZno"    : "*1.04",
          "EEChannelZno"      : "*1.04",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_MM["_JESdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.97",
          "EEChannelTT"      : "*0.97",
          "MuMuChannelTT-FullLept"    : "*0.97",
          "EEChannelTT-FullLept"      : "*0.97",
          "MuMuChannelTT-SemiLept"    : "*0.97",
          "EEChannelTT-SemiLept"      : "*0.97",
          "MuMuChannelZbb"    : "*( (1.05*(@4==2))+(1.43*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.05*(@4==2))+(1.43*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.43",
          "EEChannelZbx"      : "*1.43",
          "MuMuChannelZxx"    : "*1.09",
          "EEChannelZxx"      : "*1.09",
          "MuMuChannelZno"    : "*1.09",
          "EEChannelZno"      : "*1.09",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }


#ML SFs
SFs_fit_ML = {}
SFs_fit_ML[""]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.0",
          "EEChannelTT"      : "*1.0",
          "MuMuChannelTT-FullLept"    : "*1.0",
          "EEChannelTT-FullLept"      : "*1.0",
          "MuMuChannelTT-SemiLept"    : "*1.0",
          "EEChannelTT-SemiLept"      : "*1.0",
          "MuMuChannelZbb"    : "*( (1.06*(@4==2))+(1.22*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.06*(@4==2))+(1.22*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.22",
          "EEChannelZbx"      : "*1.22",
          "MuMuChannelZxx"    : "*1.38",
          "EEChannelZxx"      : "*1.38",
          "MuMuChannelZno"    : "*1.38",
          "EEChannelZno"      : "*1.38",
          "MuMuChannelZZ"    : "*(8.4/7.7)",
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_bcBTAGup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.97",
          "EEChannelTT"      : "*0.97",
          "MuMuChannelTT-FullLept"    : "*0.97",
          "EEChannelTT-FullLept"      : "*0.97",
          "MuMuChannelTT-SemiLept"    : "*0.97",
          "EEChannelTT-SemiLept"      : "*0.97",
          "MuMuChannelZbb"    : "*( (1.01*(@4==2))+(1.18*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.01*(@4==2))+(1.18*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.18",
          "EEChannelZbx"      : "*1.18",
          "MuMuChannelZxx"    : "*1.34",
          "EEChannelZxx"      : "*1.34",
          "MuMuChannelZno"    : "*1.34",
          "EEChannelZno"      : "*1.34",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_bcBTAGdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.03",
          "EEChannelTT"      : "*1.03",
          "MuMuChannelTT-FullLept"    : "*1.03",
          "EEChannelTT-FullLept"      : "*1.03",
          "MuMuChannelTT-SemiLept"    : "*1.03",
          "EEChannelTT-SemiLept"      : "*1.03",
          "MuMuChannelZbb"    : "*( (1.10*(@4==2))+(1.26*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.10*(@4==2))+(1.26*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.26",
          "EEChannelZbx"      : "*1.26",
          "MuMuChannelZxx"    : "*1.41",
          "EEChannelZxx"      : "*1.41",
          "MuMuChannelZno"    : "*1.41",
          "EEChannelZno"      : "*1.41",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_lBTAGup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.96",
          "EEChannelTT"      : "*0.96",
          "MuMuChannelTT-FullLept"    : "*0.96",
          "EEChannelTT-FullLept"      : "*0.96",
          "MuMuChannelTT-SemiLept"    : "*0.96",
          "EEChannelTT-SemiLept"      : "*0.96",
          "MuMuChannelZbb"    : "*( (1.06*(@4==2))+(1.21*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.06*(@4==2))+(1.21*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.21",
          "EEChannelZbx"      : "*1.21",
          "MuMuChannelZxx"    : "*1.20",
          "EEChannelZxx"      : "*1.20",
          "MuMuChannelZno"    : "*1.20",
          "EEChannelZno"      : "*1.20",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_lBTAGdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.00",
          "EEChannelTT"      : "*1.00",
          "MuMuChannelTT-FullLept"    : "*1.00",
          "EEChannelTT-FullLept"      : "*1.00",
          "MuMuChannelTT-SemiLept"    : "*1.00",
          "EEChannelTT-SemiLept"      : "*1.00",
          "MuMuChannelZbb"    : "*( (1.06*(@4==2))+(1.23*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.06*(@4==2))+(1.23*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.23",
          "EEChannelZbx"      : "*1.23",
          "MuMuChannelZxx"    : "*1.59",
          "EEChannelZxx"      : "*1.59",
          "MuMuChannelZno"    : "*1.59",
          "EEChannelZno"      : "*1.59",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_JESup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*0.99",
          "EEChannelTT"      : "*0.99",
          "MuMuChannelTT-FullLept"    : "*0.99",
          "EEChannelTT-FullLept"      : "*0.99",
          "MuMuChannelTT-SemiLept"    : "*0.99",
          "EEChannelTT-SemiLept"      : "*0.99",
          "MuMuChannelZbb"    : "*( (1.12*(@4==2))+(1.14*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.12*(@4==2))+(1.14*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.14",
          "EEChannelZbx"      : "*1.14",
          "MuMuChannelZxx"    : "*1.25",
          "EEChannelZxx"      : "*1.25",
          "MuMuChannelZno"    : "*1.25",
          "EEChannelZno"      : "*1.25",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_JERup"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.03",
          "EEChannelTT"      : "*1.03",
          "MuMuChannelTT-FullLept"    : "*1.03",
          "EEChannelTT-FullLept"      : "*1.03",
          "MuMuChannelTT-SemiLept"    : "*1.03",
          "EEChannelTT-SemiLept"      : "*1.03",
          "MuMuChannelZbb"    : "*( (1.18*(@4==2))+(1.19*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.18*(@4==2))+(1.19*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.19",
          "EEChannelZbx"      : "*1.19",
          "MuMuChannelZxx"    : "*1.24",
          "EEChannelZxx"      : "*1.24",
          "MuMuChannelZno"    : "*1.24",
          "EEChannelZno"      : "*1.24",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }

SFs_fit_ML["_JESdown"]={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.03",
          "EEChannelTT"      : "*1.03",
          "MuMuChannelTT-FullLept"    : "*1.03",
          "EEChannelTT-FullLept"      : "*1.03",
          "MuMuChannelTT-SemiLept"    : "*1.03",
          "EEChannelTT-SemiLept"      : "*1.03",
          "MuMuChannelZbb"    : "*( (0.97*(@4==2))+(1.41*(@4>2)) )",
          "EEChannelZbb"      : "*( (0.97*(@4==2))+(1.41*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.41",
          "EEChannelZbx"      : "*1.41",
          "MuMuChannelZxx"    : "*1.44",
          "EEChannelZxx"      : "*1.44",
          "MuMuChannelZno"    : "*1.44",
          "EEChannelZno"      : "*1.44",
          "MuMuChannelZZ"    : "*(8.4/7.7)", #cms meas. 5.26/fb 8 TeV 
          "EEChannelZZ"      : "*(8.4/7.7)",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          "MuMuChannelZH115" : "*1.0",
          "EEChannelZH115"   : "*1.0",
          "MuMuChannelZH120" : "*1.0",
          "EEChannelZH120"   : "*1.0",
          "MuMuChannelZH130" : "*1.0",
          "EEChannelZH130"   : "*1.0",
          "MuMuChannelZH135" : "*1.0",
          "EEChannelZH135"   : "*1.0",
          }



PlotForCLsRaw = [
    #Maximum 60 chs
    ############################################################
    #"NN_Higgs125vsDY_MM_N_CSV_2011_comb",#1
    #"NN_Higgs125vsZZ_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsTT_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsBKG_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsDY_MM_N_CSV_2012_comb_ZH125",#5
    #"NN_Higgs125vsZZ_MM_N_CSV_2012_comb_ZH125",
    #"NN_Higgs125vsTT_MM_N_CSV_2012_comb_ZH125",
    #"NN_Higgs125vsBkgcomb",
    #"NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600",
    #"NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500",#10
    #"NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000",
    #"NN_Higgs125vsBkgcomb_2_3_2_1_1000",
    #"NN_Higgs125vsBkgcomb_1_10000",
    #"NN_Higgs125vsBkgcomb_1_5000",
    #"NN_Higgs125vsBkgcomb_2_10000",#15
    #"NN_Higgs125vsBkgcomb_2_5000",
    #"NN_Higgs125vsBkgcomb_3_5000",
    #"NN_Higgs125vsBkgcomb_2_3_2_10000",
    #"NN_Higgs125vsBkgcomb_2_3_2_5000",
    #"NN_Higgs125vsBkgcomb_2_4_10000",#20
    #"NN_Higgs125vsBkgcomb_2_5_3_1_1000",
    #"NN_Higgs125vsBkgcomb_3_2_10000",
    #"NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520",
    #"NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520",
    #"NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520",#25
    #"NN_Higgs125vsBkg_2jcomb_2_2_2_500_Nj2Mbb50_200Pt402520",
    #"NN_Higgs125vsBkg_2jcomb_6_6_131_Nj2Mbb80_150Pt402520_3",
    #"NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_8",
    #"NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_21",
    #"NN_Higgs125vsBkg_2jcomb_2_500_Nj2Mbb80_150Pt402520_1",#30
    #"NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt",
    #"NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt",
    #"NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt",
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_4",
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_5",#35
    #"NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_9",
    #"NN_Higgs125vsBkg_3jcomb_9_9_300_Nj3_Mbb50_150_Pt402520_4",
    #"NN_Higgs125vsBkg_3jcomb_5_600_Nj3_Mbb50_150_Pt402520_1",
    
    #"NN_Higgs125vsDYcomb_12_120_Nj2Mbb80_150Pt402520_2",
    #"NN_Higgs125vsZZcomb_2_2_1000_Nj2Mbb80_150Pt402520",#40
    #"NN_Higgs125vsTTcomb_6_3_2_150_Nj2Mbb80_150Pt402520",
    #"NN_Higgs125vsDYcombMbbjdRbjdRbb_12_9_6_3_210_Nj3MbbPt",
    #"NN_Higgs125vsZZcombMbbjdRbjdRbb_9_100_Nj3Mbb50_150_Pt",
    #"NN_Higgs125vsTTcombMbbjdRbjdRbb_2_2_600_Nj3Mbb50_150_Pt",
    "NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520",#45 ###################
    #"NN_Higgs125vsBkg_2jcomb_4_2_500_Nj2Mbb80_150Pt402520",
    "NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt", ##################
    #"NN_Higgs125vsBkg_3jcomb_prodCSV_3_2_1000_Nj3Mbb50_150Pt",
    #"NN_ZZvsDYcomb_12_50_Nj2_Mbb45_115_Ptb1j40_Ptb2j25_Ptll20",
    #"NN_ZZvsDYcombMbbjdRbjdRbb_12_50_Nj3Mbb15_115Pt402520",#50
    #"NN_ZZvsTTcomb_2_1000_Nj2Mbb45_115Pt402520",
    #"NN_ZZvsTTcombMbbjdRbjdRbb_3_2_500_Nj3Mbb15_115Pt402520",
    "NN_ZZvsBkg_2jcomb_12_50_Nj2Mbb45_115Pt402520", #################
    "NN_ZZvsBkg_3jcomb_prodCSV_9_200_Nj3Mbb15_115Pt402520", ##############
    
    #"SumNN",
    #"ProdNN",
    #"SumWeightedNN",
    #"SumNN_2j",
    #"ProdNN_2j",
    #"SumWeightedNN_2j",
    #"SumNN_3j",
    #"ProdNN_3j",
    #"SumWeightedNN_3j",
    
    #"SumNN_ML_2j",
    #"ProdNN_ML_2j",
    #"SumWeightedNN_ML_2j",
    #"SumNN_ML_3j",
    #"ProdNN_ML_3j",
    #"SumWeightedNN_ML_3j",
      
    "bdt",
    ]

PlotForCLs = []
for plot in PlotForCLsRaw:
    PlotForCLs.append(plot)
    #for m in ["110","115","120","125","130","135","140","145","150"] :
    #for m in ["125"] :
        #PlotForCLs.append(plot+"_"+m)
        #print plot+"_"+m
blindList = PlotForCLs

namePlotList = [
     "eventSelectionbestzmassMu"  , 
     "eventSelectionbestzmassEle" ,
     "eventSelectionbestzptMu"    ,    
     "eventSelectionbestzptEle"   ,
     "jetmetbjet1pt"              ,   
     "jetmetbjet2pt"              ,   
     "jetmetbjet1CSVdisc"         ,   
     "jetmetbjet2CSVdisc"         ,
     "jetmetbjet1SSVHEdisc"         ,
     "jetmetbjet2SSVHEdisc"         ,
     "jetmetMET"                  ,
     "jetmetMETsignificance"      ,
     "eventSelectiondphiZbb"      ,
     "eventSelectiondijetPt"      ,
     "eventSelectiondijetM"       ,
     "eventSelectiondijetdR"      ,
     "eventSelectionZbbM"         ,
     "eventSelectiondrllMu"       ,
     "eventSelectiondrllEle"      ,
     "eventSelectionZbM"          ,
     "jetmetnj"                   ,
     "vertexAssociationnvertices" ,
     "jetmetbjet1beta" ,
     "jetmetbjet1betaStar" ,
     "jetmetbjet2beta" ,
     "jetmetbjet2betaStar",
     "jetmetbjet1SVmass", 
     "jetmetbjet2SVmass", 

##  #   "eventSelectiondijetSVdR"    ,
##     "eventSelectiondphiZbj1"     , 
     #"jetmetbjet1JPdisc"         ,
     #"jetmetbjet2JPdisc"         ,
     ]

namePlotListOnMC = [
    "mcSelectionnJets",
    "mcSelectionnbJets",
    "mcSelectionncJets",
    "mcSelectionllpt",
    ]


namePlotListOnMerged = [
     "jetmetbjetMinCSVdisc"   ,   
     "jetmetbjetMaxCSVdisc"   ,
     "jetmetbjetProdCSVdisc"  ,   
     "Wgg"           
     ,"Wqq"           
     ,"Wtt"           
     ,"Wzz3"          
     ,"Wzz0"           
     ,"Whi3_125"           
     ,"Whi0_125"
     ,"mlpDYvsTT_2012",

#    ,"mlpZbbvsTT_MM"
#    ,"mlpZbbvsTT_MM_N"
#    ,"mlpZbbvsTT_ML"
#    ,"mlpZbbvsTT_mu_MM"
#    ,"mlpZbbvsTT_mu_MM_N",
#    ,"mlpZbbvsTT_mu_ML"
    ]
namePlotListOnMerged+=PlotForCLs

################
### minimums ###
################
min = {
    "eventSelectionbestzmassMu" :   60 ,  
    "eventSelectionbestzmassEle":   60 ,  
    "eventSelectionbestzptMu"   :    0 ,
    "eventSelectionbestzptEle"  :    0 ,
    "eventSelectiondijetPt"     :    0 ,
    "eventSelectiondrZbj1"      :    0 ,
    "jetmetbjet1pt"             :    0 ,
    "jetmetbjet2pt"             :    0 ,   
    "jetmetbjet1CSVdisc"        :    0.679 ,
    "jetmetbjet2CSVdisc"        :    0.679 ,   
    "jetmetbjet1JPdisc"        :    0. ,
    "jetmetbjet2JPdisc"        :    0. ,
    "jetmetbjet1SSVHEdisc"        :    0. ,
    "jetmetbjet2SSVHEdisc"        :    0. , 
    "jetmetbjetMinCSVdisc"      :    0.679 ,
    "jetmetbjetMaxCSVdisc"      :    0.679 ,
    "jetmetbjetProdCSVdisc"     :    0.244*0.679 ,
#    "jetmetbjetProdCSVdisc"     :    0.679*0.679 ,
    "jetmetMET"                 :    0 , 
    "eventSelectiondphiZbj1"    :    0 ,
    "eventSelectiondphiZbb"     :    0 ,
    "eventSelectiondrZbb"       :    0 ,
    "eventSelectionscaldptZbj1" : -250 ,
    "eventSelectiondijetM"      :    0 ,
    "eventSelectiondijetdR"     :    0 ,
    "eventSelectiondijetSVdR"   :    0 ,
    "eventSelectionZbbM"        :    0 ,
    "eventSelectionZbM"         :    0 ,
    "eventSelectionZbbPt"       :    0 ,
    "jetmetjet1SSVHPdisc"       :    0 ,
    "jetmetbjet1SVmass"          :    0 ,
    "jetmetbjet2SVmass"          :    0 ,
    "eventSelectiondrllMu"      :    0 ,
    "eventSelectiondrllEle"     :    0 
    ,"jetmetnj" : 2
    ,"vertexAssociationnvertices" : -0.5
    ,"jetmetbjet1beta" : -1
    ,"jetmetbjet1betaStar" : -1
    ,"jetmetbjet2beta" : -1
    ,"jetmetbjet2betaStar" : -1
    
    ,"Wgg"      :    16 
    ,"Wqq"      :    16 
    ,"Wtt"      :    20 
#    ,"Wtwb"      :    20 
    ,"Wzz3"      :    8 
    ,"Wzz0"      :    18
    ,"Whi3_125"      :    11 
    ,"Whi0_125"      :    21 
    ,"jetmetMETsignificance" : 0
    ,"jetmetMET" : 0

    ,"mlpZbbvsTT_MM" : 0
    ,"mlpZbbvsTT_MM_N" : 0
    ,"mlpZbbvsTT_ML" : 0
    ,"mlpZbbvsTT_mu_MM" : 0
    ,"mlpZbbvsTT_mu_MM_N" : 0
    ,"mlpZbbvsTT_mu_ML" : 0,
    "mlpDYvsTT_2012": 0,

    "mcSelectionnJets" : -0.5,
    "mcSelectionnbJets" : -0.5,
    "mcSelectionncJets" : -0.5,
    "mcSelectionllpt" : 0,
    }

################
### maximums ###
################
max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  500 ,
    "eventSelectionbestzptEle"  :  500 ,
    "eventSelectiondijetPt"     :  360 ,
    "eventSelectiondrZbj1"      :    5 ,
    "jetmetbjet1pt"             :  260 ,
    "jetmetbjet2pt"             :  250 ,   
    "jetmetbjet1CSVdisc"             :  1 ,
    "jetmetbjet2CSVdisc"             :  1 ,   
    "jetmetbjet1JPdisc"             :  2.5 ,
    "jetmetbjet2JPdisc"             :  2.5 ,   
    "jetmetbjet1SSVHEdisc"             :  10 ,
    "jetmetbjet2SSVHEdisc"             :  10 ,   
    "jetmetbjetMinCSVdisc"             :    1 ,
    "jetmetbjetMaxCSVdisc"             :    1 ,
    "jetmetbjetProdCSVdisc"             :    1 ,
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :  3.2 ,
    "eventSelectiondphiZbb"     :  3.2 ,
    "eventSelectiondrZbb"       :    5 ,
    "eventSelectionscaldptZbj1" :  250 ,
    "eventSelectiondijetM"      :  480 ,
    "eventSelectiondijetdR"     :    5 ,
    "eventSelectiondijetSVdR"   :    5 ,
    "eventSelectionZbbM"        : 1000 ,
    "eventSelectionZbM"         :  800 ,
    "eventSelectionZbbPt"       :  500 ,
    "jetmetjet1SSVHPdisc"       :    8 ,
    "jetmetbjet1SVmass"          :    5 ,
    "jetmetbjet2SVmass"          :    5 ,
    "eventSelectiondrllMu"      :    5 ,
    "eventSelectiondrllEle"      :    5 
    ,"jetmetnj" :  8
    ,"vertexAssociationnvertices" : 59.5
    ,"jetmetbjet1beta" : 1
    ,"jetmetbjet1betaStar" : 1
    ,"jetmetbjet2beta" : 1
    ,"jetmetbjet2betaStar" : 1
    ,"Wgg"      :    24 
    ,"Wqq"      :    24 
    ,"Wtt"      :    30 
#    ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :   28
    ,"Whi3_125"      :    21
    ,"Whi0_125"      :    31
    ,"jetmetMETsignificance" : 20
    ,"jetmetMET" : 100

    ,"mlpZbbvsTT_MM" : 1
    ,"mlpDYvsTT_2012" : 1
    ,"mlpZbbvsTT_MM_N" : 1
    ,"mlpZbbvsTT_ML" : 1
    ,"mlpZbbvsTT_mu_MM" : 1
    ,"mlpZbbvsTT_mu_MM_N" : 1
    ,"mlpZbbvsTT_mu_ML" : 1,

    "mcSelectionnJets" : 9.5,
    "mcSelectionnbJets" : 9.5,
    "mcSelectionncJets" : 9.5,
    "mcSelectionllpt" : 500,
    }

################
### binning  ###
################
binning = {
    "eventSelectionbestzmassMu" :   24 , #2GeV 
    "eventSelectionbestzmassEle":   24 ,  
    "eventSelectionbestzptMu"   :   25 , #20GeV
    "eventSelectionbestzptEle"  :   25 ,
    "eventSelectiondijetPt"     :   18 ,
    "eventSelectiondrZbj1"      :   10 , #0.5
    "jetmetbjet1pt"             :   26 , #10GeV
    "jetmetbjet2pt"             :  500 , #0.5GeV   
    "jetmetbjet1CSVdisc"             :  20  ,
    "jetmetbjet2CSVdisc"             :  20  ,
    "jetmetbjet1JPdisc"             :  20  ,
    "jetmetbjet2JPdisc"             :  20  ,
    "jetmetbjet1SSVHEdisc"             :  60  , 
    "jetmetbjet2SSVHEdisc"             :  60  ,
    "jetmetbjetMinCSVdisc"             : 20 ,
    "jetmetbjetMaxCSVdisc"             :   20 ,
    "jetmetbjetProdCSVdisc"             :  20 ,   
    "jetmetMET"                 :   20 , #10GeV 
    "eventSelectiondphiZbj1"    :   16 , #0.2
    "eventSelectiondphiZbb"     :   16 ,
    "eventSelectiondrZbb"       :   10 , #0.5
    "eventSelectionscaldptZbj1" :   50 , #10GeV
    "eventSelectiondijetM"      :   480 , #50GeV
    "eventSelectiondijetdR"     :   10 , #0.5
    "eventSelectiondijetSVdR"   :   10 ,
    "eventSelectionZbbM"        :   20 , #50GeV
    "eventSelectionZbM"         :   16 ,
    "eventSelectionZbbPt"       :   50 , #10GeV
    "jetmetjet1SSVHPdisc"       :   16 ,
    "jetmetbjet1SVmass"          :   20 , #0.25GeV
    "jetmetbjet2SVmass"          :   20 , #0.25GeV
    "eventSelectiondrllMu"      :   10 , #0.5
    "eventSelectiondrllEle"      :   10
    ,"jetmetnj" : 6
    ,"vertexAssociationnvertices" : 60
    ,"jetmetbjet1beta" : 20
    ,"jetmetbjet1betaStar" : 20
    ,"jetmetbjet2beta" : 20
    ,"jetmetbjet2betaStar" : 20
    ,"Wgg"      :    20 
    ,"Wqq"      :    20 
    ,"Wtt"      :    25 
 #   ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :    20 
    ,"Whi3_125"      :    20 
    ,"Whi0_125"      :    20
    ,"jetmetMETsignificance" : 20
    ,"jetmetMET" : 20

    ,"mlpZbbvsTT_MM" : 20
    ,"mlpDYvsTT_2012" : 20
    ,"mlpZbbvsTT_MM_N" : 10
    ,"mlpZbbvsTT_ML" : 20
    ,"mlpZbbvsTT_mu_MM" : 20
    ,"mlpZbbvsTT_mu_MM_N" : 20
    ,"mlpZbbvsTT_mu_ML" : 20,

    "mcSelectionnJets"  : 10,
    "mcSelectionnbJets" : 10,
    "mcSelectionncJets" : 10,
    "mcSelectionllpt" : 25,
    }
    

for p in PlotForCLs :
    min[p] = 0.
    max[p] = 1.
    binning[p] = 20
    if "bdt" in p :
        min[p] = -1.
        max[p] = 1.
        binning[p] = 40
                    
