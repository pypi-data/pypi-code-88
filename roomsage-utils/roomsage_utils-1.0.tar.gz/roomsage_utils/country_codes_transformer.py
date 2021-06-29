# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 09:49:00 2017

@author: Piotr Zioło
"""


##############################
class CountryCodesTransformer:
    
    def transform_previo_code_to_iso(self, previo_country_number):
        if previo_country_number == 1:
            return "CZE"
        if previo_country_number == 468:
            return "AFG"
        if previo_country_number == 473:
            return "AND"
        if previo_country_number == 474:
            return "AGO"
        if previo_country_number == 478:
            return "ARG"
        if previo_country_number == 479:
            return "ARM"
        if previo_country_number == 481:
            return "AUS"
        if previo_country_number == 483:
            return "BHS"
        if previo_country_number == 487:
            return "BEL"
        if previo_country_number == 489:
            return "BLR"
        if previo_country_number == 495:
            return "BWA"
        if previo_country_number == 497:
            return "BRA"
        if previo_country_number == 499:
            return "VGB"
        if previo_country_number == 501:
            return "BGR"
        if previo_country_number == 506:
            return "CHN"
        if previo_country_number == 507:
            return "DNK"
        if previo_country_number == 509:
            return "DOM"
        if previo_country_number == 511:
            return "TCD"
        if previo_country_number == 512:
            return "EGY"
        if previo_country_number == 513:
            return "ECU"
        if previo_country_number == 515:
            return "EST"
        if previo_country_number == 520:
            return "PHL"
        if previo_country_number == 521:
            return "FIN"
        if previo_country_number == 522:
            return "FRA"
        if previo_country_number == 529:
            return "GEO"
        if previo_country_number == 538:
            return "HKG"
        if previo_country_number == 539:
            return "CHL"
        if previo_country_number == 540:
            return "HRV"
        if previo_country_number == 541:
            return "IND"
        if previo_country_number == 544:
            return "IRN"
        if previo_country_number == 545:
            return "IRL"
        if previo_country_number == 546:
            return "ISL"
        if previo_country_number == 547:
            return "ITA"
        if previo_country_number == 548:
            return "ISR"
        if previo_country_number == 550:
            return "JPN"
        if previo_country_number == 552:
            return "ZAF"
        if previo_country_number == 555:
            return "YUG"
        if previo_country_number == 559:
            return "CAN"
        if previo_country_number == 562:
            return "KAZ"
        if previo_country_number == 566:
            return "COL"
        if previo_country_number == 570:
            return "PRK"
        if previo_country_number == 571:
            return "KOR"
        if previo_country_number == 575:
            return "CYP"
        if previo_country_number == 579:
            return "LBN"
        if previo_country_number == 583:
            return "LTU"
        if previo_country_number == 584:
            return "LVA"
        if previo_country_number == 585:
            return "LUX"
        if previo_country_number == 587:
            return "MDG"
        if previo_country_number == 588:
            return "HUN"
        if previo_country_number == 589:
            return "MKD"
        if previo_country_number == 590:
            return "MYS"
        if previo_country_number == 595:
            return "MAR"
        if previo_country_number == 600:
            return "MEX"
        if previo_country_number == 602:
            return "MDA"
        if previo_country_number == 608:
            return "NAM"
        if previo_country_number == 610:
            return "DEU"
        if previo_country_number == 617:
            return "NLD"
        if previo_country_number == 619:
            return "NOR"
        if previo_country_number == 620:
            return "NZL"
        if previo_country_number == 630:
            return "POL"
        if previo_country_number == 632:
            return "PRT"
        if previo_country_number == 633:
            return "AUT"
        if previo_country_number == 635:
            return "ROU"
        if previo_country_number == 636:
            return "RUS"
        if previo_country_number == 638:
            return "GRC"
        if previo_country_number == 639:
            return "SLV"
        if previo_country_number == 642:
            return "SAU"
        if previo_country_number == 647:
            return "SGP"
        if previo_country_number == 648:
            return "SVK"
        if previo_country_number == 649:
            return "SVN"
        if previo_country_number == 651:
            return "ARE"
        if previo_country_number == 652:
            return "USA"
        if previo_country_number == 654:
            return "CAF"
        if previo_country_number == 666:
            return "ESP"
        if previo_country_number == 667:
            return "SWE"
        if previo_country_number == 668:
            return "CHE"
        if previo_country_number == 671:
            return "THA"
        if previo_country_number == 672:
            return "TWN"
        if previo_country_number == 678:
            return "TUR"
        if previo_country_number == 683:
            return "UKR"
        if previo_country_number == 684:
            return "URY"
        if previo_country_number == 685:
            return "UZB"
        if previo_country_number == 689:
            return "GBR"
        if previo_country_number == 691:
            return "VNM"
        if previo_country_number == 696:
            return "MNE"
        if previo_country_number == 701:
            return "RKS"
        if previo_country_number == 706:
            return "SRB"
        if previo_country_number == 707:
            return "AZE"

    def transform_two_letter_to_three_letter_iso(self, two_letter_code):
        if two_letter_code == "AF":
            return "AFG"
        if two_letter_code == "AX":
            return "ALA"
        if two_letter_code == "AL":
            return "ALB"
        if two_letter_code == "DZ":
            return "DZA"
        if two_letter_code == "AS":
            return "ASM"
        if two_letter_code == "AD":
            return "AND"
        if two_letter_code == "AO":
            return "AGO"
        if two_letter_code == "AI":
            return "AIA"
        if two_letter_code == "AQ":
            return "ATA"
        if two_letter_code == "AG":
            return "ATG"
        if two_letter_code == "AR":
            return "ARG"
        if two_letter_code == "AM":
            return "ARM"
        if two_letter_code == "AW":
            return "ABW"
        if two_letter_code == "AU":
            return "AUS"
        if two_letter_code == "AT":
            return "AUT"
        if two_letter_code == "AZ":
            return "AZE"
        if two_letter_code == "BS":
            return "BHS"
        if two_letter_code == "BH":
            return "BHR"
        if two_letter_code == "BD":
            return "BGD"
        if two_letter_code == "BB":
            return "BRB"
        if two_letter_code == "BY":
            return "BLR"
        if two_letter_code == "BE":
            return "BEL"
        if two_letter_code == "BZ":
            return "BLZ"
        if two_letter_code == "BJ":
            return "BEN"
        if two_letter_code == "BM":
            return "BMU"
        if two_letter_code == "BT":
            return "BTN"
        if two_letter_code == "BO":
            return "BOL"
        if two_letter_code == "BA":
            return "BIH"
        if two_letter_code == "BW":
            return "BWA"
        if two_letter_code == "BV":
            return "BVT"
        if two_letter_code == "BR":
            return "BRA"
        if two_letter_code == "VG":
            return "VGB"
        if two_letter_code == "IO":
            return "IOT"
        if two_letter_code == "BN":
            return "BRN"
        if two_letter_code == "BG":
            return "BGR"
        if two_letter_code == "BF":
            return "BFA"
        if two_letter_code == "BI":
            return "BDI"
        if two_letter_code == "KH":
            return "KHM"
        if two_letter_code == "CM":
            return "CMR"
        if two_letter_code == "CA":
            return "CAN"
        if two_letter_code == "CV":
            return "CPV"
        if two_letter_code == "KY":
            return "CYM"
        if two_letter_code == "CF":
            return "CAF"
        if two_letter_code == "TD":
            return "TCD"
        if two_letter_code == "CL":
            return "CHL"
        if two_letter_code == "CN":
            return "CHN"
        if two_letter_code == "HK":
            return "HKG"
        if two_letter_code == "MO":
            return "MAC"
        if two_letter_code == "CX":
            return "CXR"
        if two_letter_code == "CC":
            return "CCK"
        if two_letter_code == "CO":
            return "COL"
        if two_letter_code == "KM":
            return "COM"
        if two_letter_code == "CG":
            return "COG"
        if two_letter_code == "CD":
            return "COD"
        if two_letter_code == "CK":
            return "COK"
        if two_letter_code == "CR":
            return "CRI"
        if two_letter_code == "CI":
            return "CIV"
        if two_letter_code == "HR":
            return "HRV"
        if two_letter_code == "CU":
            return "CUB"
        if two_letter_code == "CY":
            return "CYP"
        if two_letter_code == "CZ":
            return "CZE"
        if two_letter_code == "DK":
            return "DNK"
        if two_letter_code == "DJ":
            return "DJI"
        if two_letter_code == "DM":
            return "DMA"
        if two_letter_code == "DO":
            return "DOM"
        if two_letter_code == "EC":
            return "ECU"
        if two_letter_code == "EG":
            return "EGY"
        if two_letter_code == "SV":
            return "SLV"
        if two_letter_code == "GQ":
            return "GNQ"
        if two_letter_code == "ER":
            return "ERI"
        if two_letter_code == "EE":
            return "EST"
        if two_letter_code == "ET":
            return "ETH"
        if two_letter_code == "FK":
            return "FLK"
        if two_letter_code == "FO":
            return "FRO"
        if two_letter_code == "FJ":
            return "FJI"
        if two_letter_code == "FI":
            return "FIN"
        if two_letter_code == "FR":
            return "FRA"
        if two_letter_code == "GF":
            return "GUF"
        if two_letter_code == "PF":
            return "PYF"
        if two_letter_code == "TF":
            return "ATF"
        if two_letter_code == "GA":
            return "GAB"
        if two_letter_code == "GM":
            return "GMB"
        if two_letter_code == "GE":
            return "GEO"
        if two_letter_code == "DE":
            return "DEU"
        if two_letter_code == "GH":
            return "GHA"
        if two_letter_code == "GI":
            return "GIB"
        if two_letter_code == "GR":
            return "GRC"
        if two_letter_code == "GL":
            return "GRL"
        if two_letter_code == "GD":
            return "GRD"
        if two_letter_code == "GP":
            return "GLP"
        if two_letter_code == "GU":
            return "GUM"
        if two_letter_code == "GT":
            return "GTM"
        if two_letter_code == "GG":
            return "GGY"
        if two_letter_code == "GN":
            return "GIN"
        if two_letter_code == "GW":
            return "GNB"
        if two_letter_code == "GY":
            return "GUY"
        if two_letter_code == "HT":
            return "HTI"
        if two_letter_code == "HM":
            return "HMD"
        if two_letter_code == "VA":
            return "VAT"
        if two_letter_code == "HN":
            return "HND"
        if two_letter_code == "HU":
            return "HUN"
        if two_letter_code == "IS":
            return "ISL"
        if two_letter_code == "IN":
            return "IND"
        if two_letter_code == "ID":
            return "IDN"
        if two_letter_code == "IR":
            return "IRN"
        if two_letter_code == "IQ":
            return "IRQ"
        if two_letter_code == "IE":
            return "IRL"
        if two_letter_code == "IM":
            return "IMN"
        if two_letter_code == "IL":
            return "ISR"
        if two_letter_code == "IT":
            return "ITA"
        if two_letter_code == "JM":
            return "JAM"
        if two_letter_code == "JP":
            return "JPN"
        if two_letter_code == "JE":
            return "JEY"
        if two_letter_code == "JO":
            return "JOR"
        if two_letter_code == "KZ":
            return "KAZ"
        if two_letter_code == "KE":
            return "KEN"
        if two_letter_code == "KI":
            return "KIR"
        if two_letter_code == "KP":
            return "PRK"
        if two_letter_code == "KR":
            return "KOR"
        if two_letter_code == "KW":
            return "KWT"
        if two_letter_code == "KG":
            return "KGZ"
        if two_letter_code == "LA":
            return "LAO"
        if two_letter_code == "LV":
            return "LVA"
        if two_letter_code == "LB":
            return "LBN"
        if two_letter_code == "LS":
            return "LSO"
        if two_letter_code == "LR":
            return "LBR"
        if two_letter_code == "LY":
            return "LBY"
        if two_letter_code == "LI":
            return "LIE"
        if two_letter_code == "LT":
            return "LTU"
        if two_letter_code == "LU":
            return "LUX"
        if two_letter_code == "MK":
            return "MKD"
        if two_letter_code == "MG":
            return "MDG"
        if two_letter_code == "MW":
            return "MWI"
        if two_letter_code == "MY":
            return "MYS"
        if two_letter_code == "MV":
            return "MDV"
        if two_letter_code == "ML":
            return "MLI"
        if two_letter_code == "MT":
            return "MLT"
        if two_letter_code == "MH":
            return "MHL"
        if two_letter_code == "MQ":
            return "MTQ"
        if two_letter_code == "MR":
            return "MRT"
        if two_letter_code == "MU":
            return "MUS"
        if two_letter_code == "YT":
            return "MYT"
        if two_letter_code == "MX":
            return "MEX"
        if two_letter_code == "FM":
            return "FSM"
        if two_letter_code == "MD":
            return "MDA"
        if two_letter_code == "MC":
            return "MCO"
        if two_letter_code == "MN":
            return "MNG"
        if two_letter_code == "ME":
            return "MNE"
        if two_letter_code == "MS":
            return "MSR"
        if two_letter_code == "MA":
            return "MAR"
        if two_letter_code == "MZ":
            return "MOZ"
        if two_letter_code == "MM":
            return "MMR"
        if two_letter_code == "nan":
            return "NAM"
        if two_letter_code == "NR":
            return "NRU"
        if two_letter_code == "NP":
            return "NPL"
        if two_letter_code == "NL":
            return "NLD"
        if two_letter_code == "AN":
            return "ANT"
        if two_letter_code == "NC":
            return "NCL"
        if two_letter_code == "NZ":
            return "NZL"
        if two_letter_code == "NI":
            return "NIC"
        if two_letter_code == "NE":
            return "NER"
        if two_letter_code == "NG":
            return "NGA"
        if two_letter_code == "NU":
            return "NIU"
        if two_letter_code == "NF":
            return "NFK"
        if two_letter_code == "MP":
            return "MNP"
        if two_letter_code == "NO":
            return "NOR"
        if two_letter_code == "OM":
            return "OMN"
        if two_letter_code == "PK":
            return "PAK"
        if two_letter_code == "PW":
            return "PLW"
        if two_letter_code == "PS":
            return "PSE"
        if two_letter_code == "PA":
            return "PAN"
        if two_letter_code == "PG":
            return "PNG"
        if two_letter_code == "PY":
            return "PRY"
        if two_letter_code == "PE":
            return "PER"
        if two_letter_code == "PH":
            return "PHL"
        if two_letter_code == "PN":
            return "PCN"
        if two_letter_code == "PL":
            return "POL"
        if two_letter_code == "PT":
            return "PRT"
        if two_letter_code == "PR":
            return "PRI"
        if two_letter_code == "QA":
            return "QAT"
        if two_letter_code == "RE":
            return "REU"
        if two_letter_code == "RO":
            return "ROU"
        if two_letter_code == "RU":
            return "RUS"
        if two_letter_code == "RW":
            return "RWA"
        if two_letter_code == "BL":
            return "BLM"
        if two_letter_code == "SH":
            return "SHN"
        if two_letter_code == "KN":
            return "KNA"
        if two_letter_code == "LC":
            return "LCA"
        if two_letter_code == "MF":
            return "MAF"
        if two_letter_code == "PM":
            return "SPM"
        if two_letter_code == "VC":
            return "VCT"
        if two_letter_code == "WS":
            return "WSM"
        if two_letter_code == "SM":
            return "SMR"
        if two_letter_code == "ST":
            return "STP"
        if two_letter_code == "SA":
            return "SAU"
        if two_letter_code == "SN":
            return "SEN"
        if two_letter_code == "RS":
            return "SRB"
        if two_letter_code == "SC":
            return "SYC"
        if two_letter_code == "SL":
            return "SLE"
        if two_letter_code == "SG":
            return "SGP"
        if two_letter_code == "SK":
            return "SVK"
        if two_letter_code == "SI":
            return "SVN"
        if two_letter_code == "SB":
            return "SLB"
        if two_letter_code == "SO":
            return "SOM"
        if two_letter_code == "ZA":
            return "ZAF"
        if two_letter_code == "GS":
            return "SGS"
        if two_letter_code == "SS":
            return "SSD"
        if two_letter_code == "ES":
            return "ESP"
        if two_letter_code == "LK":
            return "LKA"
        if two_letter_code == "SD":
            return "SDN"
        if two_letter_code == "SR":
            return "SUR"
        if two_letter_code == "SJ":
            return "SJM"
        if two_letter_code == "SZ":
            return "SWZ"
        if two_letter_code == "SE":
            return "SWE"
        if two_letter_code == "CH":
            return "CHE"
        if two_letter_code == "SY":
            return "SYR"
        if two_letter_code == "TW":
            return "TWN"
        if two_letter_code == "TJ":
            return "TJK"
        if two_letter_code == "TZ":
            return "TZA"
        if two_letter_code == "TH":
            return "THA"
        if two_letter_code == "TL":
            return "TLS"
        if two_letter_code == "TG":
            return "TGO"
        if two_letter_code == "TK":
            return "TKL"
        if two_letter_code == "TO":
            return "TON"
        if two_letter_code == "TT":
            return "TTO"
        if two_letter_code == "TN":
            return "TUN"
        if two_letter_code == "TR":
            return "TUR"
        if two_letter_code == "TM":
            return "TKM"
        if two_letter_code == "TC":
            return "TCA"
        if two_letter_code == "TV":
            return "TUV"
        if two_letter_code == "UG":
            return "UGA"
        if two_letter_code == "UA":
            return "UKR"
        if two_letter_code == "AE":
            return "ARE"
        if two_letter_code == "GB":
            return "GBR"
        if two_letter_code == "US":
            return "USA"
        if two_letter_code == "UM":
            return "UMI"
        if two_letter_code == "UY":
            return "URY"
        if two_letter_code == "UZ":
            return "UZB"
        if two_letter_code == "VU":
            return "VUT"
        if two_letter_code == "VE":
            return "VEN"
        if two_letter_code == "VN":
            return "VNM"
        if two_letter_code == "VI":
            return "VIR"
        if two_letter_code == "WF":
            return "WLF"
        if two_letter_code == "EH":
            return "ESH"
        if two_letter_code == "YE":
            return "YEM"
        if two_letter_code == "ZM":
            return "ZMB"
        if two_letter_code == "ZW":
            return "ZWE"

    def transform_bcom_name_to_iso(self, bcom_country_name):
        if bcom_country_name == "Czech":
            return "CZE"        
        if bcom_country_name == "Poland":
            return "POL"
        if bcom_country_name == "Lithuania":
            return "LTU"
        if bcom_country_name == "Austria":
            return "AUT"
        if bcom_country_name == "Germany":
            return "DEU"
        if bcom_country_name == "Sweden":
            return "SWE"
        if bcom_country_name == "Norway":
            return "NOR"
        if bcom_country_name == "France":
            return "FRA"
        if bcom_country_name == "Italy":
            return "ITA"
        if bcom_country_name == "United Kingdom":
            return "GBR"
        if bcom_country_name == "USA":
            return "USA"

    def transform_gadw_name_to_iso(self, gadw_country_name):
        if gadw_country_name == "Afghanistan":
            return "AFG"
        if gadw_country_name == "Aland Islands":
            return "ALA"
        if gadw_country_name == "Albania":
            return "ALB"
        if gadw_country_name == "Algeria":
            return "DZA"
        if gadw_country_name == "American Samoa":
            return "ASM"
        if gadw_country_name == "Andorra":
            return "AND"
        if gadw_country_name == "Angola":
            return "AGO"
        if gadw_country_name == "Anguilla":
            return "AIA"
        if gadw_country_name == "Antarctica":
            return "ATA"
        if gadw_country_name == "Antigua and Barbuda":
            return "ATG"
        if gadw_country_name == "Argentina":
            return "ARG"
        if gadw_country_name == "Armenia":
            return "ARM"
        if gadw_country_name == "Aruba":
            return "ABW"
        if gadw_country_name == "Australia":
            return "AUS"
        if gadw_country_name == "Austria":
            return "AUT"
        if gadw_country_name == "Azerbaijan":
            return "AZE"
        if gadw_country_name == "Bahamas":
            return "BHS"
        if gadw_country_name == "Bahrain":
            return "BHR"
        if gadw_country_name == "Bangladesh":
            return "BGD"
        if gadw_country_name == "Barbados":
            return "BRB"
        if gadw_country_name == "Belarus":
            return "BLR"
        if gadw_country_name == "Belgium":
            return "BEL"
        if gadw_country_name == "Belize":
            return "BLZ"
        if gadw_country_name == "Benin":
            return "BEN"
        if gadw_country_name == "Bermuda":
            return "BMU"
        if gadw_country_name == "Bhutan":
            return "BTN"
        if gadw_country_name == "Bolivia":
            return "BOL"
        if gadw_country_name == "Bosnia and Herzegovina":
            return "BIH"
        if gadw_country_name == "Botswana":
            return "BWA"
        if gadw_country_name == "Bouvet Island":
            return "BVT"
        if gadw_country_name == "Brazil":
            return "BRA"
        if gadw_country_name == "British Virgin Islands":
            return "VGB"
        if gadw_country_name == "British Indian Ocean Territory":
            return "IOT"
        if gadw_country_name == "Brunei Darussalam":
            return "BRN"
        if gadw_country_name == "Bulgaria":
            return "BGR"
        if gadw_country_name == "Burkina Faso":
            return "BFA"
        if gadw_country_name == "Burundi":
            return "BDI"
        if gadw_country_name == "Cambodia":
            return "KHM"
        if gadw_country_name == "Cameroon":
            return "CMR"
        if gadw_country_name == "Canada":
            return "CAN"
        if gadw_country_name == "Cape Verde":
            return "CPV"
        if gadw_country_name == "Cayman Islands":
            return "CYM"
        if gadw_country_name == "Central African Republic":
            return "CAF"
        if gadw_country_name == "Chad":
            return "TCD"
        if gadw_country_name == "Chile":
            return "CHL"
        if gadw_country_name == "China":
            return "CHN"
        if gadw_country_name == "Hong Kong, Special Administrative Region of China":
            return "HKG"
        if gadw_country_name == "Macao, Special Administrative Region of China":
            return "MAC"
        if gadw_country_name == "Macao":
            return "MAC"
        if gadw_country_name == "Macau":
            return "MAC"
        if gadw_country_name == "Christmas Island":
            return "CXR"
        if gadw_country_name == "Cocos Keeling Islands":
            return "CCK"
        if gadw_country_name == "Colombia":
            return "COL"
        if gadw_country_name == "Comoros":
            return "COM"
        if gadw_country_name == "Congo Brazzaville":
            return "COG"
        if gadw_country_name == "Congo, Democratic Republic of the":
            return "COD"
        if gadw_country_name == "Cook Islands":
            return "COK"
        if gadw_country_name == "Costa Rica":
            return "CRI"
        if gadw_country_name == "Côte d'Ivoire":
            return "CIV"
        if gadw_country_name == "Croatia":
            return "HRV"
        if gadw_country_name == "Cuba":
            return "CUB"
        if gadw_country_name == "Cyprus":
            return "CYP"
        if gadw_country_name == "Czechia":
            return "CZE"
        if gadw_country_name == "Czech Republic":
            return "CZE"
        if gadw_country_name == "Denmark":
            return "DNK"
        if gadw_country_name == "Djibouti":
            return "DJI"
        if gadw_country_name == "Dominica":
            return "DMA"
        if gadw_country_name == "Dominican Republic":
            return "DOM"
        if gadw_country_name == "Ecuador":
            return "ECU"
        if gadw_country_name == "Egypt":
            return "EGY"
        if gadw_country_name == "El Salvador":
            return "SLV"
        if gadw_country_name == "Equatorial Guinea":
            return "GNQ"
        if gadw_country_name == "Eritrea":
            return "ERI"
        if gadw_country_name == "Estonia":
            return "EST"
        if gadw_country_name == "Ethiopia":
            return "ETH"
        if gadw_country_name == "Falkland Islands Malvinas":
            return "FLK"
        if gadw_country_name == "Faroe Islands":
            return "FRO"
        if gadw_country_name == "Fiji":
            return "FJI"
        if gadw_country_name == "Finland":
            return "FIN"
        if gadw_country_name == "France":
            return "FRA"
        if gadw_country_name == "French Guiana":
            return "GUF"
        if gadw_country_name == "French Polynesia":
            return "PYF"
        if gadw_country_name == "French Southern Territories":
            return "ATF"
        if gadw_country_name == "Gabon":
            return "GAB"
        if gadw_country_name == "Gambia":
            return "GMB"
        if gadw_country_name == "Georgia":
            return "GEO"
        if gadw_country_name == "Germany":
            return "DEU"
        if gadw_country_name == "Ghana":
            return "GHA"
        if gadw_country_name == "Gibraltar":
            return "GIB"
        if gadw_country_name == "Greece":
            return "GRC"
        if gadw_country_name == "Greenland":
            return "GRL"
        if gadw_country_name == "Grenada":
            return "GRD"
        if gadw_country_name == "Guadeloupe":
            return "GLP"
        if gadw_country_name == "Guam":
            return "GUM"
        if gadw_country_name == "Guatemala":
            return "GTM"
        if gadw_country_name == "Guernsey":
            return "GGY"
        if gadw_country_name == "Guinea":
            return "GIN"
        if gadw_country_name == "Guinea-Bissau":
            return "GNB"
        if gadw_country_name == "Guyana":
            return "GUY"
        if gadw_country_name == "Haiti":
            return "HTI"
        if gadw_country_name == "Heard Island and Mcdonald Islands":
            return "HMD"
        if gadw_country_name == "Holy See Vatican City State":
            return "VAT"
        if gadw_country_name == "Honduras":
            return "HND"
        if gadw_country_name == "Hong Kong":
            return "HKG"
        if gadw_country_name == "Hungary":
            return "HUN"
        if gadw_country_name == "Iceland":
            return "ISL"
        if gadw_country_name == "India":
            return "IND"
        if gadw_country_name == "Indonesia":
            return "IDN"
        if gadw_country_name == "Iran, Islamic Republic of":
            return "IRN"
        if gadw_country_name == "Iran":
            return "IRN"
        if gadw_country_name == "Iraq":
            return "IRQ"
        if gadw_country_name == "Ireland":
            return "IRL"
        if gadw_country_name == "Isle of Man":
            return "IMN"
        if gadw_country_name == "Israel":
            return "ISR"
        if gadw_country_name == "Italy":
            return "ITA"
        if gadw_country_name == "Jamaica":
            return "JAM"
        if gadw_country_name == "Japan":
            return "JPN"
        if gadw_country_name == "Jersey":
            return "JEY"
        if gadw_country_name == "Jordan":
            return "JOR"
        if gadw_country_name == "Kazakhstan":
            return "KAZ"
        if gadw_country_name == "Kenya":
            return "KEN"
        if gadw_country_name == "Kiribati":
            return "KIR"
        if gadw_country_name == "Korea, Democratic People's Republic of":
            return "PRK"
        if gadw_country_name == "North Korea":
            return "PRK"
        if gadw_country_name == "Korea, Republic of":
            return "KOR"
        if gadw_country_name == "South Korea":
            return "KOR"
        if gadw_country_name == "Kosovo":
            return "RKS"
        if gadw_country_name == "Kuwait":
            return "KWT"
        if gadw_country_name == "Kyrgyzstan":
            return "KGZ"
        if gadw_country_name == "Lao PDR":
            return "LAO"
        if gadw_country_name == "Laos":
            return "LAO"
        if gadw_country_name == "Latvia":
            return "LVA"
        if gadw_country_name == "Lebanon":
            return "LBN"
        if gadw_country_name == "Lesotho":
            return "LSO"
        if gadw_country_name == "Liberia":
            return "LBR"
        if gadw_country_name == "Libya":
            return "LBY"
        if gadw_country_name == "Liechtenstein":
            return "LIE"
        if gadw_country_name == "Lithuania":
            return "LTU"
        if gadw_country_name == "Luxembourg":
            return "LUX"
        if gadw_country_name == "Macedonia, Republic of":
            return "MKD"
        if gadw_country_name == "Macedonia FYROM":
            return "MKD"
        if gadw_country_name == "Macedonia":
            return "MKD"
        if gadw_country_name == "Madagascar":
            return "MDG"
        if gadw_country_name == "Malawi":
            return "MWI"
        if gadw_country_name == "Malaysia":
            return "MYS"
        if gadw_country_name == "Maldives":
            return "MDV"
        if gadw_country_name == "Mali":
            return "MLI"
        if gadw_country_name == "Malta":
            return "MLT"
        if gadw_country_name == "Marshall Islands":
            return "MHL"
        if gadw_country_name == "Martinique":
            return "MTQ"
        if gadw_country_name == "Mauritania":
            return "MRT"
        if gadw_country_name == "Mauritius":
            return "MUS"
        if gadw_country_name == "Mayotte":
            return "MYT"
        if gadw_country_name == "Mexico":
            return "MEX"
        if gadw_country_name == "Micronesia, Federated States of":
            return "FSM"
        if gadw_country_name == "Moldova":
            return "MDA"
        if gadw_country_name == "Monaco":
            return "MCO"
        if gadw_country_name == "Mongolia":
            return "MNG"
        if gadw_country_name == "Montenegro":
            return "MNE"
        if gadw_country_name == "Montserrat":
            return "MSR"
        if gadw_country_name == "Morocco":
            return "MAR"
        if gadw_country_name == "Mozambique":
            return "MOZ"
        if gadw_country_name == "Myanmar":
            return "MMR"
        if gadw_country_name == "Namibia":
            return "NAM"
        if gadw_country_name == "Nauru":
            return "NRU"
        if gadw_country_name == "Nepal":
            return "NPL"
        if gadw_country_name == "Netherlands":
            return "NLD"
        if gadw_country_name == "Netherlands Antilles":
            return "ANT"
        if gadw_country_name == "New Caledonia":
            return "NCL"
        if gadw_country_name == "New Zealand":
            return "NZL"
        if gadw_country_name == "Nicaragua":
            return "NIC"
        if gadw_country_name == "Niger":
            return "NER"
        if gadw_country_name == "Nigeria":
            return "NGA"
        if gadw_country_name == "Niue":
            return "NIU"
        if gadw_country_name == "Norfolk Island":
            return "NFK"
        if gadw_country_name == "Northern Mariana Islands":
            return "MNP"
        if gadw_country_name == "Norway":
            return "NOR"
        if gadw_country_name == "Oman":
            return "OMN"
        if gadw_country_name == "Pakistan":
            return "PAK"
        if gadw_country_name == "Palau":
            return "PLW"
        if gadw_country_name == "Palestinian Territory, Occupied":
            return "PSE"
        if gadw_country_name == "Palestine":
            return "PSE"
        if gadw_country_name == "Panama":
            return "PAN"
        if gadw_country_name == "Papua New Guinea":
            return "PNG"
        if gadw_country_name == "Paraguay":
            return "PRY"
        if gadw_country_name == "Peru":
            return "PER"
        if gadw_country_name == "Philippines":
            return "PHL"
        if gadw_country_name == "Pitcairn":
            return "PCN"
        if gadw_country_name == "Poland":
            return "POL"
        if gadw_country_name == "Portugal":
            return "PRT"
        if gadw_country_name == "Puerto Rico":
            return "PRI"
        if gadw_country_name == "Qatar":
            return "QAT"
        if gadw_country_name == "Reunion":
            return "REU"
        if gadw_country_name == "Réunion":
            return "REU"
        if gadw_country_name == "Romania":
            return "ROU"
        if gadw_country_name == "Russia":
            return "RUS"
        if gadw_country_name == "Russian Federation":
            return "RUS"
        if gadw_country_name == "Rwanda":
            return "RWA"
        if gadw_country_name == "Saint-Barthélemy":
            return "BLM"
        if gadw_country_name == "Saint Helena":
            return "SHN"
        if gadw_country_name == "Saint Kitts and Nevis":
            return "KNA"
        if gadw_country_name == "Saint Lucia":
            return "LCA"
        if gadw_country_name == "Saint-Martin French part":
            return "MAF"
        if gadw_country_name == "Saint Pierre and Miquelon":
            return "SPM"
        if gadw_country_name == "Saint Vincent and Grenadines":
            return "VCT"
        if gadw_country_name == "Samoa":
            return "WSM"
        if gadw_country_name == "San Marino":
            return "SMR"
        if gadw_country_name == "Sao Tome and Principe":
            return "STP"
        if gadw_country_name == "Saudi Arabia":
            return "SAU"
        if gadw_country_name == "Senegal":
            return "SEN"
        if gadw_country_name == "Serbia":
            return "SRB"
        if gadw_country_name == "Seychelles":
            return "SYC"
        if gadw_country_name == "Sierra Leone":
            return "SLE"
        if gadw_country_name == "Singapore":
            return "SGP"
        if gadw_country_name == "Slovakia":
            return "SVK"
        if gadw_country_name == "Slovenia":
            return "SVN"
        if gadw_country_name == "Solomon Islands":
            return "SLB"
        if gadw_country_name == "Somalia":
            return "SOM"
        if gadw_country_name == "South Africa":
            return "ZAF"
        if gadw_country_name == "South Georgia and the South Sandwich Islands":
            return "SGS"
        if gadw_country_name == "South Sudan":
            return "SSD"
        if gadw_country_name == "Spain":
            return "ESP"
        if gadw_country_name == "Sri Lanka":
            return "LKA"
        if gadw_country_name == "Sudan":
            return "SDN"
        if gadw_country_name == "Suriname *":
            return "SUR"
        if gadw_country_name == "Svalbard and Jan Mayen Islands":
            return "SJM"
        if gadw_country_name == "Swaziland":
            return "SWZ"
        if gadw_country_name == "Sweden":
            return "SWE"
        if gadw_country_name == "Switzerland":
            return "CHE"
        if gadw_country_name == "Syrian Arab Republic Syria":
            return "SYR"
        if gadw_country_name == "Syria":
            return "SYR"
        if gadw_country_name == "Taiwan, Republic of China":
            return "TWN"
        if gadw_country_name == "Taiwan":
            return "TWN"
        if gadw_country_name == "Tajikistan":
            return "TJK"
        if gadw_country_name == "Tanzania *, United Republic of":
            return "TZA"
        if gadw_country_name == "Tanzania":
            return "TZA"
        if gadw_country_name == "Thailand":
            return "THA"
        if gadw_country_name == "Timor-Leste":
            return "TLS"
        if gadw_country_name == "Togo":
            return "TGO"
        if gadw_country_name == "Tokelau":
            return "TKL"
        if gadw_country_name == "Tonga":
            return "TON"
        if gadw_country_name == "Trinidad and Tobago":
            return "TTO"
        if gadw_country_name == "Tunisia":
            return "TUN"
        if gadw_country_name == "Turkey":
            return "TUR"
        if gadw_country_name == "Turkmenistan":
            return "TKM"
        if gadw_country_name == "Turks and Caicos Islands":
            return "TCA"
        if gadw_country_name == "Tuvalu":
            return "TUV"
        if gadw_country_name == "Uganda":
            return "UGA"
        if gadw_country_name == "Ukraine":
            return "UKR"
        if gadw_country_name == "United Arab Emirates":
            return "ARE"
        if gadw_country_name == "United Kingdom":
            return "GBR"
        if gadw_country_name == "United States of America":
            return "USA"
        if gadw_country_name == "United States":
            return "USA"
        if gadw_country_name == "United States Minor Outlying Islands":
            return "UMI"
        if gadw_country_name == "Uruguay":
            return "URY"
        if gadw_country_name == "Uzbekistan":
            return "UZB"
        if gadw_country_name == "Vanuatu":
            return "VUT"
        if gadw_country_name == "Venezuela Bolivarian Republic of":
            return "VEN"
        if gadw_country_name == "Venezuela":
            return "VEN"
        if gadw_country_name == "Viet Nam":
            return "VNM"
        if gadw_country_name == "Vietnam":
            return "VNM"
        if gadw_country_name == "Virgin Islands, US":
            return "VIR"
        if gadw_country_name == "U.S. Virgin Islands":
            return "VIR"
        if gadw_country_name == "Wallis and Futuna Islands":
            return "WLF"
        if gadw_country_name == "Western Sahara":
            return "ESH"
        if gadw_country_name == "Yemen":
            return "YEM"
        if gadw_country_name == "Zambia":
            return "ZMB"
        if gadw_country_name == "Zimbabwe":
            return "ZWE"


"""
Full list:

contry_id,name
"1","Czech Republic"
"468","Afghanistan"
"469","Albania"
"470","Algeria"
"471","American Samoa"
"472","American Virgin Islands"
"473","Andorra"
"474","Angola"
"475","Anguilla"
"476","Antarctica"
"477","Antigua & Barbuda"
"478","Argentina"
"479","Armenia"
"480","Aruba"
"481","Australia"
"483","Bahamas, The"
"484","Bahrain"
"485","Bangladesh"
"486","Barbados"
"487","Belgium"
"488","Belize"
"489","Belarus"
"490","Benin"
"491","Bermuda"
"492","Bhutan"
"493","Bolivia"
"494","Bosnia and Herzegovina"
"495","Botswana"
"496","Bouvet island"
"497","Brazil"
"498","British Indian Ocean Territory"
"499","British Virgin Islands"
"500","Brunei"
"501","Bulgaria"
"502","Burkina Faso"
"503","Burundi"
"504","Cook Islands"
"506","China"
"507","Denmark"
"508","Dominica"
"509","Dominican Republic"
"510","Djibouti"
"511","Chad"
"512","Egypt"
"513","Ecuador"
"514","Eritrea"
"515","Estonia"
"516","Ethiopia"
"517","Faroe Islands"
"518","Falkland Islands"
"519","Fiji"
"520","Philippines"
"521","Finland"
"522","France"
"523","Gabon"
"524","The Gambia"
"525","Ghana"
"526","Gibraltar"
"527","Grenada"
"528","Greenland"
"529","Georgia"
"530","Guam"
"531","Guatemala"
"532","Guinea"
"533","Guinea - Bissau"
"534","Guyana"
"535","Haiti"
"536","Heard Island and McDonald Islands"
"537","Honduras"
"538","Hongkong"
"539","Chile"
"540","Croatia"
"541","India"
"542","Indonesia"
"543","Iraq"
"544","Iran"
"545","Ireland"
"546","Iceland"
"547","Italy"
"548","Israel"
"549","Jamaica"
"550","Japan"
"551","Yemen"
"552","South Africa"
"553","South Georgia and the South Sandwich Islands"
"554","Jordan"
"555","Yugoslavia"
"556","Cayman Islands"
"557","Cambodia"
"558","Cameroon"
"559","Canada"
"560","Cape Verde"
"561","Qatar"
"562","Kazakhstan"
"563","Kenya"
"564","Kiribati"
"565","Cocos (Keeling) Islands"
"566","Colombia"
"567","Comoros"
"568","Congo"
"569","Congo, Democratic Republic"
"570","Korea, North"
"571","Korea, South"
"572","Costa Rica"
"573","Cuba"
"574","Kuwait"
"575","Cyprus"
"576","Kyrgyzstan"
"577","Laos"
"578","Lesotho"
"579","Lebanon"
"580","Liberia"
"581","Libya"
"582","Liechtenstein"
"583","Lithuania"
"584","Latvia"
"585","Luxembourg"
"586","Macao"
"587","Madagascar"
"588","Hungary"
"589","Macedonia"
"590","Malaysia"
"591","Malawi"
"592","Maldives"
"593","Mali"
"594","Malta"
"595","Morocco"
"596","Marshall Islands"
"597","Mauritius"
"598","Mauritania"
"599","United States Minor Outlying Islands"
"600","Mexico"
"601","Micronesia"
"602","Moldova"
"603","Monaco"
"604","Mongolia"
"605","Montserrat"
"606","Mozambique"
"607","Myanmar"
"608","Namibia"
"609","Nauru"
"610","Germany"
"611","Nepal"
"612","Niger"
"613","Nigeria"
"614","Nicaragua"
"615","Niue"
"616","Netherlands Antilles"
"617","Netherlands"
"618","Norfolk Island"
"619","Norway"
"620","New Zealand"
"621","Oman"
"622","Pakistan"
"623","Palau"
"624","Panama"
"625","Papua New Guinea"
"626","Paraguay"
"627","Peru"
"628","Pitcairn"
"629","Ivory Coast"
"630","Poland"
"631","Puerto Rico"
"632","Portugal"
"633","Austria"
"634","Equatorial Guinea"
"635","Romania"
"636","Russia"
"637","Rwanda"
"638","Greece"
"639","Salvador"
"640","Samoa"
"641","San Marino"
"642","Saudi Arabia"
"643","Senegal"
"644","Northern Mariana Islands"
"645","Seychelles"
"646","Sierra Leone"
"647","Singapore"
"648","Slovakia"
"649","Slovenia"
"650","Somalia"
"651","United Arab Emirates"
"652","USA"
"653","Sri Lanka"
"654","Central African Republic"
"655","Sudan"
"656","Suriname"
"657","Svalbard and Jan Mayen"
"658","Saint Helena"
"659","Saint Lucia"
"660","Saint Kitts and Nevis"
"661","São Tomé and Príncipe"
"662","Saint Vincent and the Grenadines"
"663","Swaziland"
"664","Syria"
"665","Solomon Islands"
"666","Spain"
"667","Sweden"
"668","Switzerland"
"669","Tajikistan"
"670","Tanzania"
"671","Thailand"
"672","Taiwan"
"673","Togo"
"674","Tokelau"
"675","Tonga"
"676","Trinidad & Tobago"
"677","Tunisia"
"678","Turkey"
"679","Turkmenistan"
"680","Turks & Caicos"
"681","Tuvalu"
"682","Uganda"
"683","Ukraine"
"684","Uruguay"
"685","Uzbekistan"
"686","Christmas Island"
"687","Vanuatu"
"688","Vatican"
"689","United Kingdom"
"690","Venezuela"
"691","Vietnam"
"692","Eastern Timor"
"693","Zambia"
"694","Western Sahara"
"695","Zimbabwe"
"696","Montenegro"
"701","Kosovo"
"706","Serbia"
"707","Azerbaijan"
"708","Aland Islands"
"710","Bonaire, Sint Eustatius and Saba"
"712","Curaçao"
"714","French Guyana"
"716","French Polynesia"
"718","The French Southern Territories"
"720","Guadeloupe"
"722","Guernsey"
"724","Isle of Man"
"726","Jersey"
"728","Martinique"
"730","Mayotte"
"732","New Caledonia"
"734","Occupied Palestinian territory"
"736","Réunion"
"738","Saint Barthélemy"
"740","Saint Martin (French part)"
"742","Saint Pierre and Miquelon"
"744","Saint Martin (Dutch part)"
"746","Republic of South Sudan"
"750","Wallis and Futuna Islands"

"""