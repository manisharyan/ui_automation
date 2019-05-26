@objects
    vehicleTrimLabel       xpath   //*[@id="VehicleTrimdiv"]//p[@class='vehicle-label']
    vechicleTrimTextBox    xpath   //select[@id="VehicleTrim"]
    doesYourTeslaText      xpath  //*[@id="autopilotenableddiv"]/div[1]/p[@class='vehicle-label']
    yesNoButtonForAutoPilot  xpath //*[@id="autopilotenableddiv"]/div[2]/div/fieldset
    yesButtonForAutoPilot  xpath  //input[@id="Yes"]
    noButtonForAutoPilot   xpath  //label[@id="No"]
    primaryUseOfTeslaText  xpath  //*[@id="primaryuseoftesladiv"]//p[@class='vehicle-label']
    primaryUseOfTeslaButton xpath //*[@id="primaryuseoftesladiv"]//fieldset
    personalButton         xpath   //input[@id="Personal"]
    businessButtonLabel    xpath  //label[@id="Business"]


= main section =

	@on *
	vehicleTrimLabel:
		height 22px
		width 120px
		css color is "#666666"
		css font-family is "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	vechicleTrimTextBox:
		height 41px
		width 259px
		css border is "1px solid #979797"
		css background-color is "#FFFFFF"

	doesYourTeslaText:
		height 22px
		width 397px
		css color is "#5C5C5C"
		css font-family is "Gotham"
		css font-size is "20px"

	yesNoButtonForAutoPilot:
		height 57px
		width 393px
		css border is "1px solid #979797"
		css border-radius is "28.5px"
		css background-color is "#E9EAEC"

	yesButtonForAutoPilot:
		height 39px
		width 159px
		css border-radius is "19.5px"
		css background-color is "#0090FF"

	noButtonForAutoPilot:
		height 18px
		width 29px
		css color is "#5C5C5C"
		css font-family is "Gotham Light"
		css font-size is "20px"
		css line-height is "19px"
		css text-align is "center"

	primaryUseOfTeslaText:
		height 22px
		width 376px
		css color is "#5C5C5C"
		css font-family is "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	primaryUseOfTeslaButton:
		height 57px
		width 393px
		css border is "1px solid #979797"
		css border-radius is "28.5px"
		css background-color is "#E9EAEC"

	personalButton:
		height 39px
		width 159px
		css border-radius is "19.5px"
		css background-color is "#0090FF"

	businessButtonLabel:
		height 18px
		width 86px
		css color is "#5C5C5C"
		css font-family is "Gotham Light"
		css font-size is "20px"
		css line-height is "19px"
		css text-align is "center"