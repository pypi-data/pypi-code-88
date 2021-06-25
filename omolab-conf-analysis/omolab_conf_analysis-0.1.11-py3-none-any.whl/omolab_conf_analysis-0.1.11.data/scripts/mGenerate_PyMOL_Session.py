#!/bin/bash

mkdir Pymol-Picture
echo "#==========================================">Visual-Script.pml
echo "#Start">>Visual-Script.pml

for file in *.xyz
do
base=`basename $file .xyz`
basepymol=`basename $file .xyz |sed -e 's/\-/\_/g' |sed -e 's/\ /\_/'`

cp "$base".xyz Pymol-Picture/"$basepymol"_orig.xyz
cp "$base".xyz Pymol-Picture/"$basepymol"_high.xyz
cp "$base".xyz Pymol-Picture/"$basepymol"_med.xyz
cp "$base".xyz Pymol-Picture/"$basepymol"_low.xyz
cp "$base".xyz Pymol-Picture/"$basepymol"_dat.xyz
echo "load "$basepymol"_orig.xyz" >>Visual-Script.pml
echo "load "$basepymol"_high.xyz" >>Visual-Script.pml
echo "load "$basepymol"_med.xyz" >>Visual-Script.pml
echo "load "$basepymol"_low.xyz" >>Visual-Script.pml
echo "load "$basepymol"_dat.xyz" >>Visual-Script.pml
echo "group "$basepymol", "$basepymol"*">>Visual-Script.pml
if [[ $1 = 'dist' ]]
then
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#DISTANCE, DISTANCES">>Visual-Script.pml
	echo "#Defining distances (dist)">>Visual-Script.pml
	echo "distance Distance_HX_"$basepymol" = (elem H) and "$basepymol"_high,  (neighbor elem H) and "$basepymol"_high, 2.0;color Grey, Distance_HX">>Visual-Script.pml
	echo "distance Distance_CX_"$basepymol" = (elem C) and "$basepymol"_high, (neighbor elem C) and "$basepymol"_high, 2.0;color Grey, Distance_CX">>Visual-Script.pml
	echo "distance Distance_HB_"$basepymol" = (elem B) and "$basepymol"_high, (elem H and neighbor elem B) and "$basepymol"_high, 2.0;color purple, Distance_HB">>Visual-Script.pml
	echo "distance Distance_HC_"$basepymol" = (elem C) and "$basepymol"_high, (elem H and neighbor elem C) and "$basepymol"_high, 2.0;color Black, Distance_HC">>Visual-Script.pml
	echo "distance Distance_HN_"$basepymol" = (elem N) and "$basepymol"_high, (elem H and neighbor elem N) and "$basepymol"_high, 2.0;color Blue, Distance_HN">>Visual-Script.pml
	echo "distance Distance_HO_"$basepymol" = (elem O) and "$basepymol"_high, (elem H and neighbor elem O) and "$basepymol"_high, 2.0;color Red, Distance_HO">>Visual-Script.pml
	echo "distance Distance_HSi_"$basepymol" = (name Si) and "$basepymol"_high, (elem H and neighbor elem Si) and "$basepymol"_high, 2.0;color Orange, Distance_HSi">>Visual-Script.pml
	echo "distance Distance_HP_"$basepymol" = (elem P) and "$basepymol"_high, (elem H and neighbor elem P) and "$basepymol"_high, 2.0;color Orange, Distance_HP">>Visual-Script.pml
	echo "distance Distance_HS_"$basepymol" = (elem S) and "$basepymol"_high, (elem H and neighbor elem S) and "$basepymol"_high, 2.0;color Orange, Distance_HS">>Visual-Script.pml
	echo "distance Distance_BC_"$basepymol" = (elem B) and "$basepymol"_high, (elem C and neighbor elem B) and "$basepymol"_high, 2.0;color Black, Distance_BC">>Visual-Script.pml
	echo "distance Distance_BN_"$basepymol" = (elem N) and "$basepymol"_high, (elem B and neighbor elem N) and "$basepymol"_high, 2.0;color Blue, Distance_BN">>Visual-Script.pml
	echo "distance Distance_BO_"$basepymol" = (elem O) and "$basepymol"_high, (elem B and neighbor elem O) and "$basepymol"_high, 2.0;color Red, Distance_BO">>Visual-Script.pml
	echo "distance Distance_CC_"$basepymol" = (elem C) and "$basepymol"_high, (elem C) and "$basepymol"_high, 1.6;color Black, Distance_CC">>Visual-Script.pml
	echo "distance Distance_CN_"$basepymol" = (elem N) and "$basepymol"_high, (elem C and neighbor elem N) and "$basepymol"_high, 2.0;color Blue, Distance_CN">>Visual-Script.pml
	echo "distance Distance_CO_"$basepymol" = (elem O) and "$basepymol"_high, (elem C and neighbor elem O) and "$basepymol"_high, 2.0;color Red, Distance_CO">>Visual-Script.pml
	echo "distance Distance_CSi_"$basepymol" = (name Si) and "$basepymol"_high, (elem C and neighbor elem Si) and "$basepymol"_high, 2.0;color Orange, Distance_CSi">>Visual-Script.pml
	echo "distance Distance_CP_"$basepymol" = (elem P) and "$basepymol"_high, (elem C and neighbor elem P) and "$basepymol"_high, 2.0;color Orange, Distance_CP">>Visual-Script.pml
	echo "distance Distance_CS_"$basepymol" = (elem S) and "$basepymol"_high, (elem C and neighbor elem S) and "$basepymol"_high, 2.0;color Orange, Distance_CS">>Visual-Script.pml
	echo "distance Distance_NN_"$basepymol" = (elem N) and "$basepymol"_high, (elem N and neighbor elem N) and "$basepymol"_high, 2.0;color Blue, Distance_NN">>Visual-Script.pml
	echo "distance Distance_NO_"$basepymol" = (elem O) and "$basepymol"_high, (elem N neighbor elem O) and "$basepymol"_high, 2.0;color Blue, Distance_NO">>Visual-Script.pml
	echo "distance Distance_NSi_"$basepymol" = (name Si) and "$basepymol"_high, (elem N and neighbor elem Si) and "$basepymol"_high, 2.0;color Orange, Distance_NSi">>Visual-Script.pml
	echo "distance Distance_NP_"$basepymol" = (elem P) and "$basepymol"_high, (elem N and neighbor elem P) and "$basepymol"_high, 2.0;color Orange, Distance_NP">>Visual-Script.pml
	echo "distance Distance_NS_"$basepymol" = (elem S) and "$basepymol"_high, (elem N and neighbor elem S) and "$basepymol"_high, 2.0;color Orange, Distance_NS">>Visual-Script.pml
	echo "distance Distance_OO_"$basepymol" = (elem O) and "$basepymol"_high, (elem O and neighbor elem O) and "$basepymol"_high, 2.0;color Red, Distance_OO">>Visual-Script.pml
	echo "distance Distance_OSi_"$basepymol" = (name Si) and "$basepymol"_high, (elem O and neighbor elem Si) and "$basepymol"_high, 2.0;color Orange, Distance_OSi">>Visual-Script.pml
	echo "distance Distance_OP_"$basepymol" = (elem P) and "$basepymol"_high, (elem O and neighbor elem P) and "$basepymol"_high, 2.0;color Orange, Distance_OP">>Visual-Script.pml
	echo "distance Distance_OS_"$basepymol" = (elem S) and "$basepymol"_high, (elem O and neighbor elem S) and "$basepymol"_high, 2.0;color Orange, Distance_OS">>Visual-Script.pml
	echo "distance Distance_PRh_"$basepymol" = (elem P) and "$basepymol"_high, (name Rh and neighbor elem P) and "$basepymol"_high, 2.5;color Orange, Distance_PRh">>Visual-Script.pml
	echo "">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#HYDROGEN-BONDING, H-BOND, H-BONDING">>Visual-Script.pml
	echo "#Defining hydrogen bonding distances (h_bond, hbond)">>Visual-Script.pml
	echo "set h_bond_cutoff_center, 3.6">>Visual-Script.pml
	echo "set h_bond_cutoff_edge, 3.2">>Visual-Script.pml
	echo "">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#TRANSITION STATE BONDS (TS, TSS, TS-BOND, TS-BONDS, TSBOND, TSBONDS)">>Visual-Script.pml
	echo "#Defining ts bonds (ts,ts_bond)">>Visual-Script.pml
	echo "distance TS_C-C_"$basepymol" = (/////C) and "$basepymol"_high, (/////C) and "$basepymol"_high, 3.0">>Visual-Script.pml
	echo "">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#STERIC (STERIC, STERICS)">>Visual-Script.pml
	echo "#Defining steric interactions between hydrogens (hh, steric, sterics)">>Visual-Script.pml
	echo "distance Steric_HH_21_"$basepymol" = (elem H) and "$basepymol"_high, (elem H) and "$basepymol"_high, 2.1; color Grey, Steric_HH_21">>Visual-Script.pml
	echo "distance Steric_HH_22_"$basepymol" = (elem H) and "$basepymol"_high, (elem H) and "$basepymol"_high, 2.2; color Grey, Steric_HH_22">>Visual-Script.pml
	echo "distance Steric_HH_23_"$basepymol" = (elem H) and "$basepymol"_high, (elem H) and "$basepymol"_high, 2.3; color Grey, Steric_HH_23">>Visual-Script.pml
	echo "distance Steric_HH_24_"$basepymol" = (elem H) and "$basepymol"_high, (elem H) and "$basepymol"_high, 2.4; color Grey, Steric_HH_24">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#ELECTROSTATIC (ELECTROSTATIC, ELECTROSTATICS, ESP, ESPS)">>Visual-Script.pml
	echo "#Defining electrostatic interactions and contacts (electrostatic, esp, esc)">>Visual-Script.pml
	echo "select XH_32, /////H and (neighbor /////N or neighbor /////O or neighbor /////S)">>Visual-Script.pml
	echo "distance Classic_ESP_NH_32_"$basepymol" = /////N, XH_32, 3.2; color Navy_Blue, Classic_ESP_NH_*">>Visual-Script.pml
	echo "distance Classic_ESP_OH_32_"$basepymol" = /////O, XH_32, 3.2; color Red, Classic_ESP_OH_*">>Visual-Script.pml
	echo "distance Classic_ESP_HX_32_"$basepymol" = XH_32 and "$basepymol"_high, (/////N or /////O or /////S) and "$basepymol"_high, 3.2; color Grey, Classic_ESP_HX_*; delete XH_32">>Visual-Script.pml
	echo "distance ESP_CH_32_"$basepymol" = (elem C) and "$basepymol"_high, ((elem H) and not (neighbor (elem H))) and "$basepymol"_high, 3.2; color Grey, ESP_CH_*">>Visual-Script.pml
	echo "distance ESP_NH_32_"$basepymol" = (elem N) and "$basepymol"_high, ((elem H) and not (neighbor (elem H))) and "$basepymol"_high, 3.2; color Navy_Blue, ESP_NH_*">>Visual-Script.pml
	echo "distance ESP_OH_32_"$basepymol" = (elem O) and "$basepymol"_high, ((elem H) and not (neighbor (elem H))) and "$basepymol"_high, 3.2; color Pink, ESP_OH_*">>Visual-Script.pml
	echo "distance ESP_SH_32_"$basepymol" = (elem S) and "$basepymol"_high, ((elem H) and not (neighbor (elem H))) and "$basepymol"_high, 3.2; color Yellow, ESP_SH_*">>Visual-Script.pml
	echo "distance ESP_BN_32_"$basepymol" = (elem B) and "$basepymol"_high, (elem N) and "$basepymol"_high, 3.2; color Pink, ESP_BN_*">>Visual-Script.pml
	echo "distance ESP_OO_32_"$basepymol" = (elem O) and "$basepymol"_high, (elem O) and "$basepymol"_high, 3.2; color Red, ESP_OO_*">>Visual-Script.pml
	echo "distance ESP_ON_32_"$basepymol" = (elem O) and "$basepymol"_high, (elem N) and "$basepymol"_high, 3.2; color purple, ESP_ON_*">>Visual-Script.pml
	echo "distance ESP_SS_32_"$basepymol" = (elem S) and "$basepymol"_high, (elem S) and "$basepymol"_high, 3.2; color sulfur, ESP_SS_*">>Visual-Script.pml
	echo "distance ESP_SO_32_"$basepymol" = (elem S) and "$basepymol"_high, (elem O) and "$basepymol"_high, 3.2; color violet, ESP_SO_*">>Visual-Script.pml
	echo "distance ESP_SN_32_"$basepymol" = (elem S) and "$basepymol"_high, (elem N) and "$basepymol"_high, 3.2; color purple, ESP_SN_*">>Visual-Script.pml
	echo "distance ESP_ClH_32_"$basepymol" = (name Cl) and "$basepymol"_high, (elem H) and "$basepymol"_high, 3.2; color Green, ESP_ClH_*">>Visual-Script.pml
	echo "">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "distance TMBond_SiO_"$basepymol" = (elem O) and "$basepymol"_high, (elem S) and "$basepymol"_high, 2.5;  Bond_SiO">>Visual-Script.pml
	echo "distance TMBond_SnO_"$basepymol" = (elem O) and "$basepymol"_high, (elem S) and "$basepymol"_high, 2.5;  Bond_SnO">>Visual-Script.pml
	echo "distance TMBond_ZnO_"$basepymol" = (elem O) and "$basepymol"_high, (elem Zn) and "$basepymol"_high, 2.5;  Bond_ZnO">>Visual-Script.pml
	echo "distance TMBond_InO_"$basepymol" = (elem O) and "$basepymol"_high, (elem In) and "$basepymol"_high, 2.5;  Bond_InO">>Visual-Script.pml
	echo "distance TMBond_GaO_"$basepymol" = (elem O) and "$basepymol"_high, (elem Ga) and "$basepymol"_high, 2.5;  Bond_GaO">>Visual-Script.pml
	echo "distance TMBond_AlO_"$basepymol" = (elem O) and "$basepymol"_high, (elem Al) and "$basepymol"_high, 2.5;  Bond_AlO">>Visual-Script.pml
	echo "">>Visual-Script.pml
	echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
	echo "#Defining all distances">>Visual-Script.pml
	echo "distance ALL_MainGroup_Distance = *, *, 1.75, 1; color Black, ALL_MainGroup_Distance">>Visual-Script.pml
	echo "distance ALL_TMGroup_Distance = *, *, 2.6, 1; color Black, ALL_TMGroup_Distance">>Visual-Script.pml
	echo "distance ALL_Distance= *, neighbor, 3.0, 1; color Black, ALL_Distance">>Visual-Script.pml

fi
echo "#------------------------------------------------------------------------------------------------------------------------------------------">>Visual-Script.pml
echo "#grouping objects">>Visual-Script.pml
echo "group "$basepymol", *_"$basepymol"">>Visual-Script.pml
echo "group "$basepymol", *_"$basepymol"">>Visual-Script.pml
echo "group "$basepymol", *_"$basepymol"">>Visual-Script.pml
echo "group "$basepymol", *_"$basepymol"">>Visual-Script.pml
echo "">>Visual-Script.pml

done

cat $SCRIPTS/Pymol-Visualize.txt >>Visual-Script.pml

mv Visual-Script.pml Pymol-Picture/Visual-Script.pml

open Pymol-Picture/Visual-Script.pml
