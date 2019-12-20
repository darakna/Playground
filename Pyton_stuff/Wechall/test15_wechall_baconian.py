def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]


bacon_string = "BaCoN's cIphEr or THE bacOnIAN CiPHer iS a meThOD oF sTEGaNOGrapHY (a METhoD Of HidIng A sECRet MeSsaGe as OpPOsEd TO a TRUe CiPHeR) dEVIseD BY francis bAcoN. a MessAge Is coNCeALED in THe pRESenTatIoN OF TexT, ratHer thaN iTs coNteNt. tO enCODe A MEsSaGe, eaCh lETter Of THe pLAInText Is rePLAcED By A groUp oF fIvE OF tHe LETterS 'a' or 'b'. ThIs REplACeMenT iS doNe acCOrdIng to tHE alPhABet of tHe BACOnIAN cIpHeR, sHoWn bElOw. NoTe: A SeCoNd vErSiOn oF BaCoN'S CiPhEr uSeS A UnIqUe cOdE FoR EaCh lEtTeR. iN OtHeR WoRdS, i aNd j eAcH HaS ItS OwN PaTtErN. tHe wRiTeR MuSt mAkE UsE Of tWo dIfFeReNt tYpEfAcEs fOr tHiS CiPhEr. AfTeR PrEpArInG A FaLsE MeSsAgE WiTh tHe sAmE NuMbEr oF LeTtErS As aLl oF ThE As aNd bS In tHe rEaL, sEcReT MeSsAgE, tWo tYpEfAcEs aRe cHoSeN, oNe tO RePrEsEnT As aNd tHe oThEr bS. tHeN EaCh lEtTeR Of tHe fAlSe mEsSaGe mUsT Be pReSeNtEd iN ThE ApPrOpRiAtE TyPeFaCe, AcCoRdInG To wHeThEr iT StAnDs fOr aN A Or a b. To dEcOdE ThE MeSsAgE, tHe rEvErSe mEtHoD Is aPpLiEd. EaCh 'TyPeFaCe 1' LeTtEr iN ThE FaLsE MeSsAgE Is rEpLaCeD WiTh aN A AnD EaCh 'TyPeFaCe 2' LeTtEr iS RePlAcEd wItH A B. tHe bAcOnIaN AlPhAbEt iS ThEn uSeD To rEcOvEr tHe oRiGiNaL MeSsAgE. aNy mEtHoD Of wRiTiNg tHe mEsSaGe tHaT AlLoWs tWo dIsTiNcT RePrEsEnTaTiOnS FoR EaCh cHaRaCtEr cAn bE UsEd fOr tHe bAcOn cIpHeR. bAcOn hImSeLf pRePaReD A BiLiTeRaL AlPhAbEt[2] FoR HaNdWrItTeN CaPiTaL AnD SmAlL LeTtErS WiTh eAcH HaViNg tWo aLtErNaTiVe fOrMs, OnE To bE UsEd aS A AnD ThE OtHeR As b. ThIs wAs pUbLiShEd aS An iLlUsTrAtEd pLaTe iN HiS De aUgMeNtIs sCiEnTiArUm (ThE AdVaNcEmEnT Of lEaRnInG). BeCaUsE AnY MeSsAgE Of tHe rIgHt lEnGtH CaN Be uSeD To cArRy tHe eNcOdInG, tHe sEcReT MeSsAgE Is eFfEcTiVeLy hIdDeN In pLaIn sIgHt. ThE FaLsE MeSsAgE CaN Be oN AnY ToPiC AnD ThUs cAn dIsTrAcT A PeRsOn sEeKiNg tO FiNd tHe rEaL MeSsAgE."
bacon_proc1 = ""
bacon_proc2 = ""
for letter in bacon_string:
    if letter >= "A" and letter <= "Z":
        bacon_proc1 = bacon_proc1 + "A"
        #bacon_proc2 = bacon_proc2 + "B"
    elif letter >= "a" and letter <= "z":
        bacon_proc1 = bacon_proc1 + "B"
        #bacon_proc2 = bacon_proc2 + "A"
    else:
        pass
        #bacon_proc1 = bacon_proc1 + letter
        #bacon_proc2 = bacon_proc2 + letter
processed_bacon_proc1 = ""
processed_bacon_proc2 = ""
dict = {"AAAAA" : "a", "AABBA" : "g", "ABBAA" : "n", "BAABA" : "t", "AAAAB" : "b", "AABBB" : "h", "ABBAB" : "o", "BAABB" : "v", "AAABA" : "c", "ABAAA" : "i", "ABBBA" : "p", "BABAA" : "w", "AAABB" : "d", "ABAAB" : "k", "ABBBB" : "q", "BABAB" : "x", "AABAA" : "e", "ABABA" : "l", "BAAAA" : "r", "BABBA" : "y", "AABAB" : "f", "ABABB" : "m", "BAAAB" : "s", "BABBB" : "z"}
dict2 = {}
print(bacon_proc1)
#print(bacon_proc2)
num = 0
letter = 1
while num <= int(len(bacon_proc1)/5):
    if bacon_proc1[num*5:(num + 1)*5] in dict:
        processed_bacon_proc1 = processed_bacon_proc1 + dict[bacon_proc1[num*5:(num + 1)*5]]
    else:
        pass
        #processed_bacon_proc1 = processed_bacon_proc1 + bacon_proc1[num*5:(num + 1)*5]

    if bacon_proc2[num * 5:(num + 1) * 5] in dict:
        processed_bacon_proc2 = processed_bacon_proc2 + dict[bacon_proc2[num * 5:(num + 1) * 5]]
    else:
        processed_bacon_proc2 = processed_bacon_proc2 + bacon_proc2[num * 5:(num + 1) * 5]
    if bacon_proc1[num*5:(num + 1)*5] not in dict2:
        dict2[bacon_proc1[num*5:(num + 1)*5]] = letter
        letter += 1
    num += 1
print(processed_bacon_proc1)
#print(processed_bacon_proc2)
print(dict)
print(dict2, letter)



