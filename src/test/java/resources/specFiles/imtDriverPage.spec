@objects
	back_Button								css  		img[class="img-back"]
    Vehicle_Icon 							css 		ul[class*="list-unstyled"] li:nth-child(1)
	Driver_Icon								css 		ul[class*="list-unstyled"] li:nth-child(2)
	Verify_Icon								css 		ul[class*="list-unstyled"] li:nth-child(3)
	Quote_Icon								css			ul[class*="list-unstyled"] li:nth-child(4)
	Purchase_Icon							css 		ul[class*="list-unstyled"] li:nth-child(5)
	Ans_Text								xpath		//div[contains(text(),'Please take a moment to answer a few questions...')]
	Policy_Holder_Details					xpath		//div[contains(text(),'Policy Holder Details')]
	Initials_Text							css			#initialsdiv div p
	Intitials_TextBox						css			#initialsdiv div+div input
	Like_To_Address_Text					css			#liketobeaddresseddiv div p
	Like_To_Address_TextBox					css			#liketobeaddresseddiv div+div input
	Legal_Name_Text							css			#legalnamediv div p
	Legal_Name_TextBox						css			#legalnamediv div+div input
	Postal_Code_Text						css			#postalcodediv div p
	Postal_Code_TextBox						css			#postalcodediv div+div input
	House_Number_Text						css			#plcyhldrHousenmbrdiv div p
	House_Number_TextBox_Part1				css			#plcyhldrHousenmbr
	House_Number_TextBox_Part2				css			#plcyhldrAddition
	Street_Name_Text						css			#streetnamediv div p
	Street_Name_TextBox						css			#streetnamediv div+div input
	City_Text								css			#citydiv div p
	City_TextBox							css			#citydiv div+div input
	Email_Address_Text						css			#emailAddressdiv div p
	Email_Address_TextBox					css			#emailAddressdiv div+div input
	Phone_Number_Text						css			#phonenumberdiv div p
	Phone_Number_TextBox					css			#phonenumberdiv div+div input
	Driver_Details_Section_Heading			xpath 		//div[contains(text(),'Driver Details')]
	DOB_Text								css			#drdobdiv div p
	DOB_TextBox								css			#drdobdiv div+div input
	Number_Damage_Text						css			#drnoofdamagediv div p
	Number_Damage_TextBox					css			#drnoofdamagediv div+div input
	Additional_Driver_Text					css			#draddadditionaldrdiv div p
	Additional_Driver_Box					xpath       //*[@id="draddadditionaldrdiv"]/div[2]/div/fieldset
	Additional_Driver_Yes					xpath		//*[@id="addadditionaldrYes"]
	Additional_Driver_No					xpath		//*[@id="addadditionaldrNo"]
	Continue_Button_Text					css			button[class="button-continue"]
    2018_MARSH_LLC_ALL_RIGHTS_RESERVED 		xpath 		//li[contains(text(),'2018 MARSH LLC. ALL RIGHTS RESERVED')]
	Privacy_Information 					xpath 		//a[contains(text(),'Privacy Information')]
	Conditions								xpath		//a[contains(text(),'Conditions')]
	About_Marsh 							xpath 		//a[contains(text(),'About Marsh')]
	Contact  								xpath 		//a[contains(text(),'Contact')]
	Netherlands_Flag						xpath		//img[contains(@src,'nlFlag.png')]
	Netherlands								xpath		//li[contains(text(),'Netherlands')]


= Main section =
	back_Button:
		height  22px
		width  49px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Ans_Text:
		height  50px
		width  744px
		css color is "#5C5C5C"
		css font-family contains  "Gotham Light"
		css font-size is "30px"
		css line-height is "50px"
		css text-align is "center"

	Policy_Holder_Details:
		height  33px
		width 306px
		css color is "#333333"
		css font-family contains "Gotham"
		css font-size is "30px"
		css line-height is "35px"

	Initials_Text:
		height  22px
		width    63px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Intitials_TextBox:
		height  41px
		width  86px
		css background-color is "#FFFFFF"

	Like_To_Address_Text:
		height  22px
		width  373px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Like_To_Address_TextBox:
		height  41px
		width  132px
		css background-color is "#FFFFFF"

	Legal_Name_Text:
		height  22px
		width  114px
		css color is "#666666"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Legal_Name_TextBox:
		height  54px
		width  498px
		css background-color is "#FFFFFF"

	Postal_Code_Text:
		height  22px
		width    119px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Postal_Code_TextBox:
		height  41px
		width    167px
		css background-color is "#FFFFFF"

	House_Number_Text:
		height  22px
		width  148px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	House_Number_TextBox_Part1:
		height  41px
		width  167px
		css background-color is "#FFFFFF"

	House_Number_TextBox_Part2:
		height  41px
		width  167px
		css background-color is "#FFFFFF"

	Street_Name_Text:
		height  22px
		width  124px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Street_Name_TextBox:
		height  41px
		width  262px
		css background-color is "#FFFFFF"

	City_Text:
		height  22px
		width  40px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	City_TextBox:
		height  41px
		width  262px
		css background-color is "#FFFFFF"

	Email_Address_Text:
		height  22px
		width  141px
		css color is "#5C5C5C"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Email_Address_TextBox:
		height  41px
		width  398px
		css background-color is "#FFFFFF"

	Phone_Number_Text:
		height  44px
		width  149px
		css color is "#CC0000"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Phone_Number_TextBox:
		height  41px
		width  398px
		css background-color is "#FFFFFF"

	Driver_Details_Section_Heading:
		height  33px
		width  199px
		css color is "#333333"
		css font-family contains "Gotham"
		css font-size is "30px"
		css line-height is "35px"

	DOB_Text:
		height  22px
		width  291px
		css color is "#666666"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	DOB_TextBox:
		height  41px
		width  259px
		css background-color is "#FFFFFF"

	Number_Damage_Text:
		height  22px
		width  300px
		css color is "#666666"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	Number_Damage_TextBox:
		height  41px
		width  136px
		css background-color is "#FFFFFF"

	Additional_Driver_Text:
		height  18px
		width  421px
		css color is "#5C5C5C"
		css font-family contains "Gotham Light"
		css font-size is "20px"
		css line-height is "19px"

	Additional_Driver_Box:
		height  41px
		width  435px
		css background-color is "#FFFFFF"

	Continue_Button_Text:
		height  50px
		width  217px
		css background-color is "#CC0000"


	2018_MARSH_LLC_ALL_RIGHTS_RESERVED:
		height    14px
		width    252px
		css color is   "#5C5C5C"
		css font-family contains    "Helvetica Neue"
		css font-size  is  "12px"
		css line-height  is  "14px"

	Privacy_Information:
		height 14px
		width 252px
		css color is "#5C5C5C"
		css font-family contains "Helvetica Neue"
		css font-size is "12px"
		css line-height is "14px"

	Conditions:
		height 14px
		width 59px
		css color is "#0090FF"
		css font-family contains "Helvetica Neue"
		css font-size is "12px"
		css line-height is "14px"

	About_Marsh:
		height 14px
		width 70px
		css color is "#0090FF"
		css font-family contains "Helvetica Neue"
		css font-size is "12px"
		css line-height is "14px"

	Contact:
		height 14px
		width 43px
		css color is "#0090FF"
		css font-family contains "Helvetica Neue"
		css font-size is "12px"
		css line-height is "14px"

	Netherlands_Flag:
		height 10px
		width 15px

	Netherlands:
		height 14px
		width 65px
		css color is "#5C5C5C"
		css font-family contains  "Helvetica Neue"
		css font-size is "12px"
		css line-height is "14px"