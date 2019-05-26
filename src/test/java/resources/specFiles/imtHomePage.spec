@objects
    INSURE                                      xpath       //a[@class='navbar-brand']
	CONDITIONS                                  xpath		//a[contains(text(),'CONDITIONS')]
	FAQS										xpath		//a[contains(text(),'FAQS')]
	SIGNIN										xpath		//a[contains(text(),'SIGN IN')]
	CONDITIONS_FAQS_SIGNIN                      xpath       //a[@class='navbar-brand pull-right']

	Car_Image									xpath 		//img[contains(@src,'red tesla-model-s.png')]

	OutsideWelcomeText_EntireBox				xpath 		//div[@class='row rowspace justify-content-md-center']
	InsideWelcomeText_EntireBox                 xpath       //div[@class='row rowspace justify-content-md-center']/div[@class='col-md-12 text-center']
	Welcome										xpath		//div[contains(text(),'Welcome')]
	Do_You_Know_Text							xpath		//div[contains(text(),Do you know your license plate number?')]
	This_Will_Save_Text							xpath		//div[contains(text(),'This will save you some time filling out information about your vehicle.')]

	Flag										xpath		//img[@class='flag']
	Plate_Number								xpath		//input[@formcontrolname='plateNumber']

	Continue_button								xpath		//button/strong
	Continue_button_Text						xpath 		//button[@class='nl-button-continue-hide']

	If_not_Text									xpath		/html/body/app-root/div[2]/app-licence/div/div[3]/div/div
	Skip_Link									xpath		//a[text()='skip']

	2018_MARSH_LLC_ALL_RIGHTS_RESERVED 			xpath 		//li[contains(text(),'2018 MARSH LLC. ALL RIGHTS RESERVED')]
	Privacy_Information 						xpath 		//a[contains(text(),'Privacy Information')]
	Conditions									xpath		//a[contains(text(),'Conditions')]
	About_Marsh 								xpath 		//a[contains(text(),'About Marsh')]
	Contact  									xpath 		//a[contains(text(),'Contact')]
	Netherlands_Flag							xpath		//img[contains(@src,'nlFlag.png')]
	Netherlands									xpath		//li[contains(text(),'Netherlands')]

= Main section =
    INSURE:
		aligned horizontally all CONDITIONS_FAQS_SIGNIN

	CONDITIONS:
		aligned horizontally all FAQS

	FAQS:
		aligned horizontally all SIGNIN

	SIGNIN:
		aligned horizontally all CONDITIONS

	Car_Image:
		image file expectedImages\mg1.png, error 10%
		height 272px
		width 1011px
        aligned vertically centered WelcomeText_EntireBox

	OutsideWelcomeText_EntireBox:
		height 150px
		width 873px
		css color is "#37424A"
		css font-family contains "Gotham Light"
		css font-size is "25px"
		css line-heightn is "50px"
		css text-align is "centered"
		aligned vertically centered Plate_Number
		aligned vertically centered InsideWelcomeText_EntireBox

	Plate_Number:
		css box-sizing is "border-box"
		height 67.5px
		width 448.5px
		css background-color is "#FFFFFF"
		aligned horizontally centered flag

	Flag:
		height 67px
		width 48px

	Continue_button:
		height 50px
		width 217px
		css background-color is "#CC0000"
		aligned vertically centered Continue_button_Text

	Continue_button_Text:
		height 12px
		width 121.52px
		css color is "#FFFFFF"
		css font-family contains "Gotham Medium"
		css font-size is "14px"
		css  line-height is "13px"
		css  text-align is "centered"
		aligned vertically centered Plate_Number


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

	If_not_Text:
        aligned horizontally bottom Skip_Link

    Skip_Link:
        aligned horizontally bottom If_not_Text
