######################################################################################
###                                                                                 ###
### selectionCuts_fromRDS.py                                                        ###
###                                                                                 ###
### Small script to estimate the number of events                                   ###
### for different data and MC samples                                               ###
### for a certain working point and selection                                       ###
### inspired by getYileds_fromRDS.py                                                ###
### to be used doing :                                                              ###
### python selectionCuts_fromRDS.py >> yields.txt                                   ###
### you will find the yields table at the end of yields.txt                         ###
### Also histograms are produced and store in root files                            ###
### One root files is created by sample                                             ###
### The variables listed below are ploted for each channel and for each set of cuts ### 
### To combine them, use : combinePlots_forRDSanalyser.py (after sumChannels.C)     ###
#######################################################################################

from ROOT import *
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
lib_path2 = os.path.abspath('../analysisScripts/')
from eventSelection import categoryNames
from zbbCommons import rmPixelMisAligRuns
from listForRDS import sampleList, totsampleList, sigMCsampleList, MCsampleList, bkgMCsampleList, lumi, dataPeriods, Extra_norm, namePlotList, namePlotListOnMerged, min, max, binning, PlotForCLs, SFs_fit_MM, SFs_fit_ML, blindList, DYrew, namePlotListOnMC
from globalLists import pathMergedRDS, pathRDS
import os, sys

#####################################################
### sample/wp/selection of interest
#####################################################

recreate = True
runOnMergedRDS = True
goToCLs = False
syst = ""
if len(sys.argv)>1 : syst=sys.argv[1]
mass="125"
if "ZH"+mass not in sigMCsampleList:
    print "ERROR look to higgs mass"
    exit()
DirOut="PlotsSR_SFs_MM"
useMCTruth = True
useSFs = True
useDYptBins = True
useDYjetBins = False
runPixRange = ""
if rmPixelMisAligRuns : runPixRange = "&eventSelectionrun>=207883&eventSelectionrun<=208307"
doRew = False
#here you could choose the root ouput dir
os.system('mkdir '+DirOut)

btagWP = "HPHP" #choose between HE, HP, HEHE, HEHP, HPHP
llMassWP = "" #"" or "wide"
metWP = "MET" #"MET" or "", MET means met significance

if goToCLs : DirOut="CLs_"+DirOut
if "ZH"+mass not in sigMCsampleList and len(sigMCsampleList)>0:
    print "ERROR look to higgs mass"
    exit()
            
if useMCTruth and "Zno" in totsampleList:
    totsampleList.remove("Zno")
    MCsampleList.remove("Zno")
    bkgMCsampleList.remove("Zno")

wp = 0
for cat in categoryNames:
    if cat.find(btagWP)>-1:
        if (llMassWP=="" and cat.find("wide")==-1) or (llMassWP=="wide" and cat.find(btagWP)>-1):
            if (metWP=="" and cat.find("MET")==-1)  or (metWP=="MET" and cat.find("significance")>-1):
                break
    wp+=1

WP=str(wp)

channels  = [
    "EEChannel",
    "MuMuChannel",
    ]

#choose you set of cuts
extraCuts = [
    #"",
    #"jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",

    "(eventSelectiondijetM<80||eventSelectiondijetM>150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "(eventSelectiondijetM<50||eventSelectiondijetM>150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",

    #for ZH SR
    "(eventSelectiondijetM>80&&eventSelectiondijetM<150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "(eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    #for ZZ SR
    "(eventSelectiondijetM>45&&eventSelectiondijetM<115) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    "(eventSelectiondijetM>15&&eventSelectiondijetM<115) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",

    #"(eventSelectiondijetM>80&&eventSelectiondijetM<150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520_125>0.5",
    #"(eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt_125>0.5",
    #"(eventSelectiondijetM>80&&eventSelectiondijetM<150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520_125>0.75",
    #"(eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt_125>0.75",
    #"(eventSelectiondijetM>80&&eventSelectiondijetM<150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_2jcomb_4_5000_Nj2Mbb80_150Pt402520_125>0.85",
    #"(eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20) && NN_Higgs125vsBkg_3jcomb_prodCSV_5_3_1000_Nj3Mbb50_150Pt_125>0.85",

    #"( ((eventSelectiondijetM<80||eventSelectiondijetM>150) && jetmetnj==2) || ((eventSelectiondijetM<50||eventSelectiondijetM>150) && jetmetnj>2) ) && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
    #"( ((eventSelectiondijetM>80||eventSelectiondijetM<150) && jetmetnj==2) || ((eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2) ) && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
        

#    "jetmetbjet1pt>40&jetmetbjet2pt>25",
#    "(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
#    "(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25",    
#    "jetmetnj==2&eventSelectiondijetM<150&eventSelectiondijetM>80",
#    "jetmetnj==2&jetmetbjet1pt>40&jetmetbjet2pt>25&eventSelectiondijetM<150&eventSelectiondijetM>80",
#    "jetmetnj==2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
#    "jetmetnj==2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25&eventSelectiondijetM<150&eventSelectiondijetM>80",
#    "jetmetnj>2&eventSelectiondijetM<150&eventSelectiondijetM>50",
#    "jetmetnj>2&jetmetbjet1pt>40&jetmetbjet2pt>25&eventSelectiondijetM<150&eventSelectiondijetM>50",
#    "jetmetnj>2&jetmetbjet1pt>40&jetmetbjet2pt>25&eventSelectiondphiZbb>1.5&eventSelectiondijetM<150&eventSelectiondijetM>50",
#    "jetmetnj>2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
#    "jetmetnj>2&(eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)&jetmetbjet1pt>40&jetmetbjet2pt>25",    
    #"vertexAssociationnvertices<13",
    #"vertexAssociationnvertices>=13&vertexAssociationnvertices<=17",
    #"vertexAssociationnvertices>17",
#    "(eventSelectiondijetM>80&eventSelectiondijetM<150)",
    #"newmlphiggsvsbkg_125_comb_MM_N<0.5&newmlphiggsvsbkg_125_comb_MM_N>=0.",
    #"newmlphiggsvsbkg_125_comb_MM_N>=0.5&newmlphiggsvsbkg_125_comb_MM_N<=1",
    #"ProdNN<0.5&ProdNN>=0.",
    #"ProdNN>=0.5&ProdNN<=1",
    #"SumWeightedNN<0.5&SumWeightedNN>=0.",
    #"SumWeightedNN>=0.5&SumWeightedNN<=1",
#    "jetmetbjet1pt>30",
#    "jetmetbjet2pt>30",
#    "jetmetbjet1pt>30&(eventSelectiondijetM<80||eventSelectiondijetM>150)",
#    "jetmetbjet2pt>30&(eventSelectiondijetM<80||eventSelectiondijetM>150)",

    ]

if goToCLs:
    precut = " && (eventSelectiondijetM>15&&eventSelectiondijetM<150) && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)"
    extraCuts = [
        "(eventSelectiondijetM>80&&eventSelectiondijetM<150) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
        "(eventSelectiondijetM>50&&eventSelectiondijetM<150) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
        #"(eventSelectiondijetM>45&&eventSelectiondijetM<115) && jetmetnj==2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
        #"(eventSelectiondijetM>15&&eventSelectiondijetM<115) && jetmetnj>2 && jetmetbjet1pt>40 && jetmetbjet2pt>25 && (eventSelectionbestzptEle>20||eventSelectionbestzptMu>20)",
        ]
else : precut = ""

extraCutsLep = {
    "EEChannel"     : "(eventSelectionbestzmassEle>76.&eventSelectionbestzmassEle<106.)",
    "MuMuChannel"   : "(eventSelectionbestzmassMu>76.&eventSelectionbestzmassMu<106.)"
    }

stringCut = {}
#titleCut = {}

for i in range(0,len(extraCuts)) :
    stringCut[extraCuts[i]]="Cut"+str(i+1)
    #if titleCuts[i] : titleCut[extraCuts[i]]=titleCuts[i]
    #titleCut[extraCuts[i]]=""

#####################################################
### settings (this should move somewhere central) ### 
#####################################################

MCweight = {}

for sample in MCsampleList:
    for channel in channels :
        print "the lumi of ", sample, " = ", lumi[sample]
        MCweight[channel+sample] = lumi["DATA"]/lumi[sample]/Extra_norm[channel+sample]
        print "the weight of ", channel+sample," = ", MCweight[channel+sample]

#############
### files ###
#############

myRDS_el    = {}
myRDS_mu    = {}
myRDS       = {}
myRDS_red   = {} 
myRDS_red_w = {}

path = pathMergedRDS
if not runOnMergedRDS : path = pathRDS
if goToCLs :
    for p in path :
        if not "Data" in p : path[p] = path[p].replace("Tree2_537","Tree2_537"+syst)
for sample in sampleList :
    print sample
    if sample=="DATA" or ("DY" in sample and sample[-1]=="0" and not useDYptBins) or ("DY" in sample and sample[-1]=="j" and not useDYjetBins) : continue
    redStage = "rc_eventSelection_"+WP+"==1"
    for channel in channels:
        print "Channel : ", channel
        if channel=="EEChannel" : file_mc  = TFile(path[sample+"_El_MC"])
        else : file_mc  = TFile(path[sample+"_Mu_MC"])

        tree_zbb1 = file_mc.Get("rds_zbb")
        tmpfile=TFile(DirOut+"/tmp.root","RECREATE")
        tree_zbb=tree_zbb1.CopyTree(redStage.replace("==","_idx==")+precut)
        ws_zbb = file_mc.Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)

        nEntries = rds_zbb.numEntries()
        if sample == "DY" :
            if not useMCTruth :
                myRDS[channel+"Zbb"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==6")
                myRDS[channel+"Zbx"] = rds_zbb.reduce(redStage + "&mcSelectioneventType>=4&mcSelectioneventType<6")
                myRDS[channel+"Zxx"] = rds_zbb.reduce(redStage + "&mcSelectioneventType<4&mcSelectioneventType>0")
                myRDS[channel+"Zno"] = rds_zbb.reduce(redStage + "&mcSelectioneventType==0")
            else :
                myRDS[channel+"Zbb"] = rds_zbb.reduce(redStage + "&(abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5 & jetmetnj>1)")
                myRDS[channel+"Zbx"] = rds_zbb.reduce(redStage + "&( (abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5)  & jetmetnj>1)")
                myRDS[channel+"Zxx"] = rds_zbb.reduce(redStage + "&( (abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5 & jetmetnj>1) || jetmetnj==1 )")
            print "myRDS.numEntries() for ", "Zbb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbb"].numEntries()
            print "myRDS.numEntries() for ", "Zbx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbx"].numEntries()
            print "myRDS.numEntries() for ", "Zxx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zxx"].numEntries()
            if not useMCTruth : print "myRDS.numEntries() for ", "Zno" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zno"].numEntries()
        elif ("DY" in sample and sample[-1]=="0" and useDYptBins) or ("DY" in sample and sample[-1]=="j" and useDYjetBins) :
            if not useMCTruth :
                myRDS[channel+"Zbb"].append(rds_zbb.reduce(redStage + "&mcSelectioneventType==6"))
                myRDS[channel+"Zbx"].append(rds_zbb.reduce(redStage + "&mcSelectioneventType>=4&mcSelectioneventType<6"))
                myRDS[channel+"Zxx"].append(rds_zbb.reduce(redStage + "&mcSelectioneventType<4&mcSelectioneventType>0"))
                myRDS[channel+"Zno"].append(rds_zbb.reduce(redStage + "&mcSelectioneventType==0"))
            else :
                myRDS[channel+"Zbb"].append(rds_zbb.reduce(redStage + "&abs(jetmetbjet1Flavor)==5 & abs(jetmetbjet2Flavor)==5"))
                myRDS[channel+"Zbx"].append(rds_zbb.reduce(redStage + "&( (abs(jetmetbjet1Flavor)!=5&abs(jetmetbjet2Flavor)==5) || (abs(jetmetbjet1Flavor)==5&abs(jetmetbjet2Flavor)!=5) )"))
                myRDS[channel+"Zxx"].append(rds_zbb.reduce(redStage + "&abs(jetmetbjet1Flavor)!=5 & abs(jetmetbjet2Flavor)!=5"))
            print "myRDS.numEntries() for ", "Zbb" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbb"].numEntries()
            print "myRDS.numEntries() for ", "Zbx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zbx"].numEntries()
            print "myRDS.numEntries() for ", "Zxx" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zxx"].numEntries()
            if not useMCTruth : print "myRDS.numEntries() for ", "Zno" , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"Zno"].numEntries()
        else :
            myRDS[channel+sample] = rds_zbb.reduce(redStage)
            print "myRDS.numEntries() for ", sample , " = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+sample].numEntries()
            
        file_mc.Close()

for channel in channels:
    if not "DATA" in sampleList : break
    print "Channel : ", channel
    file={}
    for period in dataPeriods :
        if channel=="EEChannel": 
            file[period]  = TFile(path["DoubleEle_Data"+period])
        else:
            file[period]  = TFile(path["DoubleMu_Data"+period])
        
    tree_zbb1 = file["A"].Get("rds_zbb")
    tmpfile=TFile(DirOut+"/tmp.root","RECREATE")
    tree_zbb=tree_zbb1.CopyTree(redStage.replace("==","_idx==")+precut)
    ws_zbb = file["A"].Get("ws_ras")
    ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
    rds_zbb = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)

    for period in dataPeriods :
        if period=="A" : continue
        tree_zbb1 = file[period].Get("rds_zbb")
        tmpfile=TFile(DirOut+"/tmp.root","RECREATE")
        tree_zbb=tree_zbb1.CopyTree(redStage.replace("==","_idx==")+precut)
        ws_zbb = file[period].Get("ws_ras")
        ras_zbb = RooArgSet(ws_zbb.allVars(),ws_zbb.allCats())
        tmp = RooDataSet("rds_zbb","rds_zbb",tree_zbb,ras_zbb)
        rds_zbb.append(tmp)
    nEntries = rds_zbb.numEntries()
    myRDS[channel+"DATA"] = rds_zbb.reduce(redStage + runPixRange)
    print "myRDS.numEntries() for DATA = ", nEntries, ". After stage ", WP, " : ", myRDS[channel+"DATA"].numEntries()
    for period in dataPeriods : file[period].Close()
    
###############
### weights ###
###############
for myrds in myRDS:
    if "DATA" in myrds : continue
    tmpRDS=myrds
    break
tmp=myRDS[tmpRDS].reduce("mcSelectioneventType==1")
ras_zbb = tmp.get()
tmp=0

btagRew = [
    "BtaggingReweightingHE"  ,
    "BtaggingReweightingHP"  ,
    "BtaggingReweightingHEHE",
    "BtaggingReweightingHEHP",
    "BtaggingReweightingHPHP",
    ]

for b in btagRew:
    if b.find(btagWP)>-1 : 
        rrv_w_b=ras_zbb[b]
        break
rrv_w_lep  = ras_zbb["LeptonsReweightingweight"]
rrv_w_lumi = ras_zbb["lumiReweightingLumiWeight"]
rrv_w_ptz = {
    "MuMuChannel" : ras_zbb["eventSelectionbestzptMu"],
    "EEChannel" : ras_zbb["eventSelectionbestzptEle"]
}
rrv_w_llpt  = ras_zbb["mcSelectionllpt"]
rrv_w_nj = ras_zbb["mcSelectionnJets"]
rrv_w_b1Flav  = ras_zbb["mcSelectionllpt"]
rrv_w_b2Flav = ras_zbb["mcSelectionnJets"]
                     
w = {}
rewFormula = {}
SFs_fit=SFs_fit_MM[syst]
if btagWP=="HEHP" : SFs_fit=SFs_fit_ML[syst]

if useDYjetBins : njFormula = "*( (@4==0)*1.+(@4==1)*"+DYrew["1j"]+"+(@4==2)*"+DYrew["2j"]+"+(@4==3)*"+DYrew["3j"]+"+(@4==4)*"+DYrew["4j"]+"+(@4>4)*1. )"
else : njFormula = "*1."

listzptrew = [0.000664024, -0.00357095, -0.00767076, -0.00967366, -0.0134844, -0.0157148, -0.0181885, -0.0209647, -0.0232788, -0.0252373, -0.0265634, -0.0275069, -0.0285776, -0.0281683, -0.0294206, -0.0299975, -0.0308047, -0.0311716, -0.030913, -0.0324821, -0.0323192, -0.0324639, -0.0319356, -0.0322621, -0.0331146, -0.0338905, -0.0345189, -0.0358591, -0.0358407, -0.040018, -0.0396389, -0.0407177, -0.0445103, -0.0441406, -0.0471215, -0.0463301, -0.0513777, -0.0536773, -0.0546446, -0.0568508, -0.0590333, -0.0612157, -0.0633981, -0.0655805, -0.067763, -0.0699454, -0.0721278, -0.0743103, -0.0764927, -0.0786751, -0.0808575, -0.08304, -0.0852224, -0.0874048, -0.0895872, -0.0917697, -0.0939521, -0.0961345, -0.098317, -0.100499, -0.102682, -0.104864, -0.107047, -0.109229, -0.111412, -0.113594, -0.115776, -0.117959, -0.120141, -0.122324, -0.124506, -0.126689, -0.128871, -0.131053, -0.133236, -0.135418, -0.137601, -0.139783, -0.141965, -0.144148, -0.14633, -0.148513, -0.150695, -0.152878, -0.15506, -0.157242, -0.159425, -0.161607, -0.16379, -0.165972, -0.168155, -0.170337, -0.172519, -0.174702, -0.176884]
zptrew="*("
for i in range(0,len(listzptrew)):
    if i==0 : zptrew+="(@3<25.)*("+str(1+listzptrew[i])+")"
    elif i==94 : zptrew+="+(@3>=490.)*("+str(1+listzptrew[i])+"))"
    else : zptrew+="+(@3>="+str(5*(i-1)+25)+")*(@3<"+str(5*i+25)+")*("+str(1+listzptrew[i])+")"
print zptrew
    
    
for channel in channels :
    if runOnMergedRDS and not "JES" in syst : ext="Extra_norm"
    else : ext=""
    if useDYptBins : llptFormula = "*( (@3<50.)*1.+(@3>=50.)*(@3<70.)*"+DYrew[channel+"DY50-70"+ext]+"+(@3>=70.)*(@3<100.)*"+DYrew[channel+"DY70-100"+ext]+"+(@3>=100.)*(@3<180.)*"+DYrew[channel+"DY100"+ext]+"+(@3>=180.)*"+DYrew[channel+"DY180"+ext]+" )"
#if useDYptBins : llptFormula = "*( (@3<50.)*1.+(@3>=50.)*(@3<70.)*"+DYrew["50-70"]+"+(@3>=70.)*(@3<100.)*"+DYrew["70-100"]+"+(@3>=100.)*(@3<180.)*"+DYrew["100-180"]+"+(@3>=180.)*"+DYrew["180"]+" )"
    else : llptFormula = "*1."
    if doRew :
        if channel=="EEChannel" : rewFormula[channel] = "*(1172.93/1391.86)*((0.945437+0.00378645*20)*(@5<20)+(0.945437+0.00378645*@5)*(@5>20)*(@5<200)+(0.945437+0.00378645*200.)*(@5>200))"
        else : rewFormula[channel] = "*(1606.22/1913.74)*((0.945437+0.00378645*20)*(@5<20)+(0.945437+0.00378645*@5)*(@5>20)*(@5<200)+(0.945437+0.00378645*200.)*(@5>200))"
    else : rewFormula[channel] = "*1."
    for sample in totsampleList :
        if "ZH" in sample:
            rewFormula[channel]=zptrew
        if "DY" in sample :
            Extra_norm[channel+sample] = Extra_norm[channel+"Zxx"]
            SFs_fit[channel+sample]  = SFs_fit[channel+"Zxx"]
        rescale=1./Extra_norm[channel+sample]
        if not runOnMergedRDS or "JES" in syst : rescale=1.
        if useSFs : SF=SFs_fit[channel+sample]
        else : SF="*1."
        if not sample in ["Zno","Zxx","Zbx","Zbb"] and "ZH" not in sample:
            w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale)+SF, RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi))
            print "reweighting formula for : ", channel, "@0*@1*@2*"+str(rescale)+SF
        elif not sample in ["Zbx","Zbb"] and "ZH" not in sample:
            w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale)+SF+llptFormula+njFormula, RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_llpt,rrv_w_nj))
            print "reweighting formula for : ", channel, "@0*@1*@2*"+str(rescale)+SF+llptFormula+njFormula
        elif sample in ["Zbx","Zbb"] :
            w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale)+SF+rewFormula[channel]+llptFormula+njFormula, RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_llpt,rrv_w_nj,rrv_w_ptz[channel]))
            print "reweighting formula for : ", channel, "@0*@1*@2*"+str(rescale)+SF+rewFormula[channel]+llptFormula+njFormula
        else :
            w[channel+sample]=RooFormulaVar("w","w", "@0*@1*@2*"+str(rescale)+SF+rewFormula[channel], RooArgList(rrv_w_b,rrv_w_lep,rrv_w_lumi,rrv_w_ptz[channel]))
#############
### PLOTS ###
#############
        
if runOnMergedRDS : namePlotList+=namePlotListOnMerged
var = {}
for name in namePlotList:
    tmpname=name
    if name in PlotForCLs and not "bdt" in name and not "ZZvs" in name : tmpname+="_"+mass
    print "name = ", name
    var[tmpname] = ras_zbb[tmpname]
    var[tmpname].setMin(min[name])
    var[tmpname].setMax(max[name])
    var[tmpname].setBins(binning[name])

th1 = {}

#################################  
### working point & selection ###
#################################

sumbkgMC = {}
sumsigMC = {}
sumDATA = {}
nevts = {}
rdh = {}

for channel in channels :
    print "channel ... ", channel
    for sample in totsampleList :
        print "sample ... ", sample
        for cut in extraCuts :
            if cut=="" : iCut=extraCutsLep[channel]
            else : iCut=cut+"&"+extraCutsLep[channel]
            print "cuts ... ", iCut
            
            myRDS_red = myRDS[channel+sample]

            print "myRDS_red.numEntries()", myRDS_red.numEntries()

            if iCut : myRDS_red = myRDS_red.reduce(iCut)
            
            if sample != "DATA": myRDS_red.addColumn(w[channel+sample])
                
            if sample != "DATA": myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get(),"","w")
            else               : myRDS_red_w = RooDataSet("myRDS_red_w","myRDS_red_w",myRDS_red,myRDS_red.get())

            nevts["pure"+sample+channel+cut]     = myRDS_red_w.numEntries()
            print "myRDS_red_w.numEntries()", myRDS_red_w.numEntries()
            if sample in MCsampleList :
                nevts["effective"+sample+channel+cut]= myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                nevts["weighted"+sample+channel+cut] = myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            
            if sample in bkgMCsampleList :
                if sample==bkgMCsampleList[0]:
                    sumbkgMC["pure"+channel+cut]     = 0
                    sumbkgMC["effective"+channel+cut]= 0
                    sumbkgMC["weighted"+channel+cut] = 0
                sumbkgMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumbkgMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumbkgMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            sumsigMC["pure"+channel+cut]     = 0
            sumsigMC["effective"+channel+cut]= 0
            sumsigMC["weighted"+channel+cut] = 0
            if sample in sigMCsampleList :
                sumsigMC["pure"+channel+cut]+=myRDS_red_w.numEntries()
                sumsigMC["effective"+channel+cut]+=myRDS_red_w.numEntries()*(lumi["DATA"]/lumi[sample])
                sumsigMC["weighted"+channel+cut]+=myRDS_red_w.sumEntries()*(lumi["DATA"]/lumi[sample])
            if sample=="DATA":
                sumDATA[channel+cut]=myRDS_red_w.numEntries()
            for name in namePlotList:
                if sample=="DATA" and name in namePlotListOnMC : continue
                if not goToCLs :
                    if name in PlotForCLs and not "bdt" in name and not "ZZvs" in name : name+="_"+mass
                    th1[channel+sample+name+cut] = TH1D(name,name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
                    if (name in blindList or name[:-4] in blindList) and sample=="DATA":
                        overflow=0
                        for bin in range(1,th1[channel+sample+name+cut].GetNbinsX()+1) :
                            if th1[channel+sample+name+cut].GetBinCenter(bin) > 0.5:
                                overflow+=th1[channel+sample+name+cut].GetBinContent(bin)
                                th1[channel+sample+name+cut].SetBinContent(bin,0)
                                th1[channel+sample+name+cut].SetBinError(bin,0)                                
                        th1[channel+sample+name+cut].SetBinContent(th1[channel+sample+name+cut].GetNbinsX(),overflow)
                    elif name=="eventSelectiondijetM"  and sample=="DATA":
                        if "jetmetnj==2" in cut :
                            if "(eventSelectiondijetM>80&&eventSelectiondijetM<150)" in cut or "(eventSelectiondijetM<80||eventSelectiondijetM>150)" in cut : cutmbb=80.
                            else : cutmbb=0.
                        elif "(eventSelectiondijetM>50&&eventSelectiondijetM<150)" in cut or "(eventSelectiondijetM<50||eventSelectiondijetM>150)" in cut : cutmbb=50.
                        else : cutmbb=0.
                        for bin in range(1,th1[channel+sample+name+cut].GetNbinsX()+1) :
                            if th1[channel+sample+name+cut].GetBinCenter(bin) > 0.5:
                                mbb=th1[channel+sample+name+cut].GetBinCenter(bin)
                                if mbb>cutmbb and mbb<150. : th1[channel+sample+name+cut].SetBinContent(bin,0)                                                        
                                if mbb>cutmbb and mbb<150. : th1[channel+sample+name+cut].SetBinError(bin,0)                                
                else :
                    if not name in PlotForCLs : continue
                    if not "bdt" in name and not "ZZvs" in name : name+="_"+mass
                    samp=sample
                    if sample == "DATA" : samp="data_obs"
                    if "ZH" in sample : samp = sample.replace("ZH","signal")
                    #if not "ZH" in sample : samp=samp+name[-3:]
                    th1[channel+sample+name+cut] = TH1D(name+samp+syst.replace("up","Up").replace("down","Down"),name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                    myRDS_red_w.fillHistogram(th1[channel+sample+name+cut], RooArgList(var[name]))
                    if syst!="" : continue
                    rdh[channel+sample+name+cut] = RooDataHist("rdh_"+channel+sample+name+cut, "rdh_"+channel+sample+name+cut, RooArgSet(var[name]),myRDS_red)
				      
                    for bin in range(0,var[name].getBins()):       
                        if bin < (var[name].getBins()/2) : continue
                        Binras = rdh[channel+sample+name+cut].get(bin)
                        a, b = Double(1), Double(1)
                        rdh[channel+sample+name+cut].weightError(a,b)
                        aw = rdh[channel+sample+name+cut].weight()
                        #print "factor",a,b , "nbr entries= ",aw 
                        if aw>0 : a=a/aw
                        if aw>0 : b=b/aw
                        th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"]= TH1D(name+samp+"_"+channel+stringCut[cut]+samp+"stat_bin"+str(bin+1)+"Up",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                        myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"], RooArgList(var[name]))
                        th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"]= TH1D(name+samp+"_"+channel+stringCut[cut]+samp+"stat_bin"+str(bin+1)+"Down",name,var[name].getBins(),var[name].getMin(),var[name].getMax())
                        myRDS_red_w.fillHistogram(th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"], RooArgList(var[name]))
                        tmp = th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].GetBinContent(bin+1)
                        if aw>0 :
                            th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp*(1.+b))
                            th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"].SetBinContent(bin+1,tmp*(1.-a))
                        else :
                            th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].SetBinContent(bin+1,tmp+b)	    
                            #print "bin", bin+1 ,"--- nominal =",tmp," --- variation Up =",b, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Up"].GetBinContent(bin+1)," --- variation Down =",a, th1[channel+sample+name+cut+"stat"+str(bin+1)+"Down"].GetBinContent(bin+1)
		
            
#################
### printouts ###
#################
print " "
print " "
print "**************************************************************************************************************************"
print "*** DATA/MC COMPARISONS***************************************************************************************************"
print "**************************************************************************************************************************"
print "working point ... ", WP
print "**************************************************************************************************************************"
print "systematic ... ", syst
print "**************************************************************************************************************************"
print "runOnMergedRDS ... ", runOnMergedRDS
print "**************************************************************************************************************************"
print "goToCLs ... ", goToCLs
print "**************************************************************************************************************************"
print "higgs mass ... ", mass
print "**************************************************************************************************************************"
print "DirOut ... ", DirOut
print "**************************************************************************************************************************"
print "z pt rew ? ... ", doRew
print "**************************************************************************************************************************"
print "useSFs ... ", useSFs
print "**************************************************************************************************************************"
print "useMCTruth ... ", useMCTruth
print "**************************************************************************************************************************"
print "useDYptBins ... ", useDYptBins
print "**************************************************************************************************************************"
print "useDYjetBins ... ", useDYjetBins
print "**************************************************************************************************************************"
print "misaligned runPixRange cut ? ... ", runPixRange
print "**************************************************************************************************************************"

for channel in channels:
    print "............................................................................"
    print "Channel ..", channel, "....................................................."
    print " "
    print "pure MC yields  ............................................................"
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+channel+cut]),
        if len(bkgMCsampleList)>0 : print '{0}'.ljust(10).format(sumbkgMC["pure"+channel+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+channel+cut])
        else : print '{0}'.ljust(10).format(sumsigMC["pure"+channel+cut])
    print " "
    print "normalized MC yields ......................................................."
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+channel+cut]).ljust(10),
        if len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["effective"+channel+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+channel+cut]).ljust(10)
        else : print '{0:.2f}'.format(sumsigMC["effective"+channel+cut]).ljust(10)
    print " "
    print "weighted and normalized MC yields vs DATA yield ............................"
    print "Cuts".ljust(10),
    for sample in MCsampleList : print sample.ljust(10),
    print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
    for cut in extraCuts:
        print stringCut[cut].ljust(10),
        for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+channel+cut]).ljust(10),
        if "DATA" in sampleList and len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["weighted"+channel+cut]).ljust(10), '{0:.2f}'.format( sumsigMC["weighted"+channel+cut]).ljust(10), '{0}'.ljust(10).format( nevts["pure"+"DATA"+channel+cut])
        elif len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["weighted"+channel+cut]).ljust(10), '{0:.2f}'.format( sumsigMC["weighted"+channel+cut]).ljust(10)
        else : print '{0:.2f}'.format( sumsigMC["weighted"+channel+cut]).ljust(10)
    print "............................................................................"
    print "............................................................................"
    print " "
    print " "

print "............................................................................"
print "Channel .. Combined ........................................................"
print " "
print "pure MC yields  ............................................................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0}'.ljust(10).format(nevts["pure"+sample+"EEChannel"+cut]+nevts["pure"+sample+"MuMuChannel"+cut]),
    if len(bkgMCsampleList)>0 : print '{0}'.ljust(10).format(sumbkgMC["pure"+"EEChannel"+cut]+sumbkgMC["pure"+"MuMuChannel"+cut]), '{0}'.ljust(10).format(sumsigMC["pure"+"EEChannel"+cut]+sumsigMC["pure"+"MuMuChannel"+cut])
    else : print '{0}'.ljust(10).format(sumsigMC["pure"+"EEChannel"+cut]+sumsigMC["pure"+"MuMuChannel"+cut])
print " "
print "normalized MC yields ......................................................."
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["effective"+sample+"EEChannel"+cut]+nevts["effective"+sample+"MuMuChannel"+cut]).ljust(10),
    if len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["effective"+"EEChannel"+cut]+sumbkgMC["effective"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["effective"+"EEChannel"+cut]+sumsigMC["effective"+"MuMuChannel"+cut]).ljust(10)
    else : print '{0:.2f}'.format(sumsigMC["effective"+"EEChannel"+cut]+sumsigMC["effective"+"MuMuChannel"+cut]).ljust(10)
print " "
print "weighted and normalized MC yields vs DATA yield ............................"
print "Cuts".ljust(10),
for sample in MCsampleList : print sample.ljust(10),
print "totbkgMC".ljust(10), "totsigMC".ljust(10), "DATA".ljust(10)
for cut in extraCuts:
    print stringCut[cut].ljust(10),
    for sample in MCsampleList : print '{0:.2f}'.format(nevts["weighted"+sample+"EEChannel"+cut]+nevts["weighted"+sample+"MuMuChannel"+cut]).ljust(10),
    if "DATA" in sampleList and len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["weighted"+"EEChannel"+cut]+sumbkgMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["weighted"+"EEChannel"+cut]+sumsigMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0}'.ljust(10).format(nevts["pure"+"DATA"+"EEChannel"+cut]+nevts["pure"+"DATA"+"MuMuChannel"+cut])
    elif len(bkgMCsampleList)>0 : print '{0:.2f}'.format(sumbkgMC["weighted"+"EEChannel"+cut]+sumbkgMC["weighted"+"MuMuChannel"+cut]).ljust(10), '{0:.2f}'.format(sumsigMC["weighted"+"EEChannel"+cut]+sumsigMC["weighted"+"MuMuChannel"+cut]).ljust(10)
    else : print '{0:.2f}'.format(sumsigMC["weighted"+"EEChannel"+cut]+sumsigMC["weighted"+"MuMuChannel"+cut]).ljust(10)
print "............................................................................"
print "............................................................................"
print " "
print " "

#################
###  outputs  ###
#################
   
file={}

if goToCLs :
    if recreate : file["Out"]=TFile(DirOut+"/histoStage"+WP+"extraCuts.root","RECREATE")
    else : file["Out"]=TFile(DirOut+"/histoStage"+WP+"extraCuts.root","UPDATE")
    for channel in channels:
        if channel=="Combined" : continue
        if recreate : chDir=file["Out"].mkdir(channel,channel)
        else : chDir=file["Out"].Get(channel)
        file["Out"].cd(channel)
        for cut in extraCuts:
            if recreate : chDir.mkdir(stringCut[cut],cut)
            chDir.cd(stringCut[cut])                            
            for sample in totsampleList:
                for name in namePlotList:
                    if not name in PlotForCLs : continue
                    if not "bdt" in name and not "ZZvs" in name :
                        name+="_"+mass
                    if not sample == "DATA" : th1[channel+sample+name+cut].Scale(lumi["DATA"]/lumi[sample])
                    
                    if chDir.Get(stringCut[cut]+"/"+th1[channel+sample+name+cut].GetName()) :
                        tmpDir=file["Out"].Get(channel+"/"+stringCut[cut])
                        #print "removing", th1[channel+sample+name+cut].GetName()
                        tmpDir.Delete(th1[channel+sample+name+cut].GetName()+";*")

                    th1[channel+sample+name+cut].Write()
                    if syst!="" : continue
                    Nbin=th1[channel+sample+name+cut].GetNbinsX();
                    for bin in range(1,Nbin+1):
                        if bin < (Nbin/2+1) : continue
                        if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Scale(lumi["DATA"]/lumi[sample])
                        th1[channel+sample+name+cut+"stat"+str(bin)+"Down"].Write()
                        if not sample == "DATA" :th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Scale(lumi["DATA"]/lumi[sample])
                        th1[channel+sample+name+cut+"stat"+str(bin)+"Up"].Write()
    file["Out"].Close()
else :
    for sample in totsampleList:
        file[sample]=TFile(DirOut+"/histoStage"+WP+"extraCuts"+sample+".root","RECREATE")
        for channel in channels:
            if channel=="Combined" : continue
            chDir=file[sample].mkdir(channel,channel)
            for cut in extraCuts:
                chDir.mkdir(stringCut[cut],cut)
                chDir.cd(stringCut[cut])
                for name in namePlotList:
                    if name in PlotForCLs and not "bdt" in name and not "ZZvs" in name : name+="_"+mass
                    #if sample=="DATA" and name in namePlotListOnMC : continue
                    if not channel+sample+name+cut in th1 : continue
                    th1[channel+sample+name+cut].Write()
        file[sample].Close()

os.system('rm '+DirOut+'/tmp.root')
