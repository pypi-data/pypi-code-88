##### Register #####

inputRegister = {
    "show": "",
    "otp": "",
    "Mobile1": "",
    "tm_sex": "",
    "tm_firstname": "",
    "tm_lastname": "",
    "tm_birthdate": "",
    "tm_number": "",
    "tm_soi": "",
    "tm_road": "",
    "tm_district": "",
    "tm_limits": "",
    "tm_province": "",
    "tm_id_number": "",
    "tm_refbrcode": "",
    "ref_tmrefcode": "",
    "res_rescode": "",
    "res_tmrefcode": ""    
}

##### SetMember #####

inputSetMember = {
    "show": "",
    "otp": "",
    "Mobile1": "",
    "tm_sex": "",
    "tm_firstname": "",
    "tm_lastname": "",
    "tm_birthdate": "",
    "tm_number": "",
    "tm_soi": "",
    "tm_road": "",
    "tm_district": "",
    "tm_limits": "",
    "tm_province": "",
    "tm_id_number": "",
    "tm_refbrcode": "",
    "ref_tmrefcode": "",
    "res_rescode": "",
    "res_tmrefcode": ""    
}

##### GetMember #####

inputGetMember = {
    "tm_code": "",
    "tm_refcode": "",
    "mobile": ""
}

responseGetMember = {
    "tm_code": "",
    "tm_type": "",
    "tm_name": "",
    "tm_expire": "",
    "tm_begin": "",
    "tm_discpct": "",
    "tm_cash": "",
    "tm_credit": "",
    "tm_crdiscpct": "",
    "tm_phone": "",
    "Mobile1": "",
    "tm_refcode": "",
}

##### RemoveMember #####

inputRemoveMember = {
    "tm_code": "",
    "tm_refcode": "",
    "mobile": ""
}

##### ChangePhone #####

inputChangePhone = {
    "tm_code": "",
    "tm_refcode": "",
    "mobile": "",
    "newphone": ""
}

##### GetBalance #####

inputGetBalance = {
    "tm_code": "",
    "tm_refcode": "",
    "mobile": ""
}

responseGetBalance = {
    "tm_code": "",
    "tm_refcode": "",
    "mp_point": 0,
    "mp_storedate": "",
    "mp_expirepoint": 0,
    "mp_expiredate": "",
    "mp_stamp": 0,
    "mp_stamp_expiredate": ""
}

##### RedeemPoint #####

inputRedeemPoint = {
    "rp_transcode": "",
    "rp_tm_code": "",
    "rp_tm_refcode": "",
    "rp_ropno": "",
    "rp_custname": "",
    "rp_phoneno": "",
    "rp_total": "",
    "rp_point": "",
    "rd_brcode": "",
    "rd_posno": "",
    "rd_refno": "",
    "rd_storedate": ""
}

##### TransferPoint #####

inputTransferPoint = {
    "tm_code": "",
    "newtm_code": ""
}

##### Get Notify #####

inputDigioGetNotify = {
    "transaction_id": "",
    "merchant_id": "",
    "terminal_id": "",
    "transaction_type": ""
}

responseDigioGetNotify = {
    "merchant_id": "",
    "merchant_name": "",
    "transaction_id": "",
    "amount": "",
    "transaction_type": "",
    "consumer_name": "",
    "mobile": "",
    "terminal_id": "",
    "transaction_date_time": ""
}

#### ---- Digio Functions ---- ####

##### Register (Vplus Registration) #####

digioInputVplusRegister = {
    "tm_title": "",
    "tm_sex": "",
    "tm_firstname": "",
    "tm_lastname": "",
    "tm_engname": "",
    "tm_englastname": "",
    "tm_birthdate": "",
    "tm_number": "",
    "tm_building": "",
    "tm_floor": "",
    "tm_soi": "",
    "tm_road": "",
    "tm_district": "",
    "tm_limits": "",
    "tm_province": "",
    "tm_postnumber": "",
    "tm_id_number": "",
    "tm_id_building": "",
    "tm_id_floor": "",
    "tm_id_soi": "",
    "tm_id_road": "",
    "tm_id_district": "",
    "tm_id_limits": "",
    "tm_id_province": "",
    "tm_id_postnumber": "",
    "tm_delivery_number": "",
    "tm_delivery_building": "",
    "tm_delivery_floor": "",
    "tm_delivery_soi": "",
    "tm_delivery_road": "",
    "tm_delivery_district": "",
    "tm_delivery_limits": "",
    "tm_delivery_province": "",
    "tm_delivery_postnumber": "",
    "tm_email": "",
    "tm_company": "",
    "tm_nacode": "",
    "tm_edcode": "",
    "tm_occode": "",
    "tm_no_chidbe12": "",
    "tm_no_chidov12": "",
    "Land1": "",
    "Land2": "",
    "Mobile1": "",
    "Mobile2": "",
    "tm_idcard": "",
    "tm_passport": "",
    "tm_single": "",
    "tm_married": "",
    "tm_salary": "",
    "tm_at_alcohol": "",
    "tm_at_softdrink": "",
    "tm_at_cookie": "",
    "tm_at_delicatessen": "",
    "tm_at_frozenfood": "",
    "tm_at_freshmeat": "",
    "tm_at_freshfruit": "",
    "tm_at_oil": "",
    "tm_at_houshold": "",
    "tm_at_health": "",
    "tm_at_Instant": "",
    "tm_at_Other": "",
    "tm_at_DairyFood": "",
    "tm_at_FreshBakery": "",
    "tm_at_Grocery": "",
    "tm_wallet_flag": ""
}

digioResponseVplusRegister = {
    "res_code": "",
    "res_desc": "",
    "tm_refcode": ""
}

##### Vplus Inquiry #####

digioInputVplusInquiry = {
    "tm_refcode": "",
    "mobile": ""
}

digioResponseVplusInquiry = {
    "res_code": "",
    "res_desc": "",
    "tm_refcode": "",
    "tm_title": "",
    "tm_sex": "",
    "tm_firstname": "",
    "tm_lastname": "",
    "tm_engname": "",
    "tm_englastname": "",
    "tm_birthdate": "",
    "tm_number": "",
    "tm_building": "",
    "tm_floor": "",
    "tm_soi": "",
    "tm_road": "",
    "tm_district": "",
    "tm_limits": "",
    "tm_province": "",
    "tm_postnumber": "",
    "tm_id_number": "",
    "tm_id_building": "",
    "tm_id_floor": "",
    "tm_id_soi": "",
    "tm_id_road": "",
    "tm_id_district": "",
    "tm_id_limits": "",
    "tm_id_province": "",
    "tm_id_postnumber": "",
    "tm_delivery_number": "",
    "tm_delivery_building": "",
    "tm_delivery_floor": "",
    "tm_delivery_soi": "",
    "tm_delivery_road": "",
    "tm_delivery_district": "",
    "tm_delivery_limits": "",
    "tm_delivery_province": "",
    "tm_delivery_postnumber": "",
    "tm_email": "",
    "tm_company": "",
    "tm_nacode": "",
    "tm_edcode": "",
    "tm_occode": "",
    "tm_no_chidbe12": "",
    "tm_no_chidov12": "",
    "Land1": "",
    "Land2": "",
    "Mobile1": "",
    "Mobile2": "",
    "tm_idcard": "",
    "tm_passport": "",
    "tm_single": "",
    "tm_married": "",
    "tm_salary": "",
    "tm_at_alcohol": "",
    "tm_at_softdrink": "",
    "tm_at_cookie": "",
    "tm_at_delicatessen": "",
    "tm_at_frozenfood": "",
    "tm_at_freshmeat": "",
    "tm_at_freshfruit": "",
    "tm_at_oil": "",
    "tm_at_houshold": "",
    "tm_at_health": "",
    "tm_at_Instant": "",
    "tm_at_Other": "",
    "tm_at_DairyFood": "",
    "tm_at_FreshBakery": "",
    "tm_at_Grocery": "",
    "tm_wallet_flag": ""
}

##### SetMember (Vplus Update) #####

digioInputVplusUpdate = {
    "tm_refcode": "",
    "tm_title": "",
    "tm_sex": "",
    "tm_firstname": "",
    "tm_lastname": "",
    "tm_engname": "",
    "tm_englastname": "",
    "tm_birthdate": "",
    "tm_number": "",
    "tm_building": "",
    "tm_floor": "",
    "tm_soi": "",
    "tm_road": "",
    "tm_district": "",
    "tm_limits": "",
    "tm_province": "",
    "tm_postnumber": "",
    "tm_id_number": "",
    "tm_id_building": "",
    "tm_id_floor": "",
    "tm_id_soi": "",
    "tm_id_road": "",
    "tm_id_district": "",
    "tm_id_limits": "",
    "tm_id_province": "",
    "tm_id_postnumber": "",
    "tm_delivery_number": "",
    "tm_delivery_building": "",
    "tm_delivery_floor": "",
    "tm_delivery_soi": "",
    "tm_delivery_road": "",
    "tm_delivery_district": "",
    "tm_delivery_limits": "",
    "tm_delivery_province": "",
    "tm_delivery_postnumber": "",
    "tm_email": "",
    "tm_company": "",
    "tm_nacode": "",
    "tm_edcode": "",
    "tm_occode": "",
    "tm_no_chidbe12": "",
    "tm_no_chidov12": "",
    "Land1": "",
    "Land2": "",
    "Mobile2": "",
    "tm_idcard": "",
    "tm_passport": "",
    "tm_single": "",
    "tm_married": "",
    "tm_salary": "",
    "tm_at_alcohol": "",
    "tm_at_softdrink": "",
    "tm_at_cookie": "",
    "tm_at_delicatessen": "",
    "tm_at_frozenfood": "",
    "tm_at_freshmeat": "",
    "tm_at_freshfruit": "",
    "tm_at_oil": "",
    "tm_at_houshold": "",
    "tm_at_health": "",
    "tm_at_Instant": "",
    "tm_at_Other": "",
    "tm_at_DairyFood": "",
    "tm_at_FreshBakery": "",
    "tm_at_Grocery": "",
    "tm_wallet_flag": ""
}

digioResponseVplusUpdate = {
    "res_code": "",
    "res_desc": ""
}

##### Inquiry Point #####

digioInputInquiryPoint = {
    "tm_refcode": ""
}

digioResponseInquiryPoint = {
    "res_code": "",
    "res_desc": "",
    "tm_type": "",
    "tm_refcode": "",
    "mp_point": "",
    "mp_storedate": "",
    "mp_stampoption": "",
    "mp_stamp": "",
    "mp_stampdate": "",
    "mp_expoption": "",
    "mp_expirepoint": "",
    "mp_expiredate": ""
}

##### Royal Orchid Plus #####

digioInputRoyalOrchidPlus = {
    "rp_tm_refcode": "",
    "rp_ropno": "",
    "rp_custname": "",
    "rp_phoneno": "",
    "rp_point": "",
    "rd_brcode": "",
    "rd_posno": "",
    "rd_refno": "",
    "rd_storedate": ""
}

digioResponseRoyalOrchidPlus = {
    "res_code": "",
    "res_desc": ""
}

##### GetNotify Transaction #####

digioInputSetNotifyTransaction = {
    "merchant_id": "",
    "merchant_name": "",
    "transaction_id": "",
    "amount": "",
    "transaction_type": "",
    "consumer_name": "",
    "mobile": "",
    "terminal_id": "",
    "transaction_date_time": ""
}

digioResponseSetNotifyTransaction = {
    "res_code": "",
    "res_desc": ""
}

##### Redeem Point #####

# commonInputRedeemPoint = {
#     "rp_tm_code": "",
#     "rp_tm_refcode": "",
#     "rp_ropno": "",
#     "rp_custname": "",
#     "rp_phoneno": "",
#     "rp_total": "",
#     "rp_point": "",
#     "rd_brcode": "",
#     "rd_posno": "",
#     "rd_refno": "",
#     "rd_storedate": ""
# }
