@objects
    please-take-a-moment  xpath  //div[@class='please-take-a-moment']
    doesYourTeslaText     xpath  //*[@id="autopilotenableddiv"]/div[1]/p[@class='vehicle-label']
	yesButtonForAutoPilot xpath  //input[@id="Yes"]
	noButtonForAutoPilot  xpath  //label[@id="No"]
	yesNoButtonForAutoPilot  xpath //*[@id="autopilotenableddiv"]/div[2]/div/fieldset
	primaryUseOfTeslaText  xpath  //*[@id="primaryuseoftesladiv"]//p[@class='vehicle-label']
	primaryUseOfTeslaButton xpath //*[@id="primaryuseoftesladiv"]//fieldset
	personalButton        xpath   //input[@id="Personal"]
	businessButton        xpath  //label[@id="Business"]
	businessUseTypeText   xpath  //*[@id="BusinessUseTypediv"]/div[1]/p
	businessUseTypeButton xpath  //*[@id="BusinessUseTypediv"]/div[2]/div/fieldset
	rentalCarText         xpath  //label[@id="RentalCar"]
	taxiLabel             xpath  //label[@id="Taxi"]
	deliveryLabel         xpath  //label[@id="Delivery"]
	securityLabel         xpath  //label[@id="Security"]
	drivingLabel          xpath  //label[@id="DrivingInstructor"]
	emergencyText         xpath  //label[@id="EmergencyServices"]
	otherButton           xpath  //input[@id="Other"]
	includeExcludeButton  xpath  //*[@id="CatalogValueinclvatdiv"]/div[2]/div/fieldset
	includeButton         xpath  //input[@id="Including"]
	excludeLabel          xpath  //label[@id="Excluding"]
	includeExcludeTaxLabel xpath //*[@id="CatalogValueinclvatdiv"]/div[1]/p
	catalogValueText     xpath   //*[@id="CatlogValueincltesladiv"]//p[@class='vehicle-label']
	catalogValueTextBox  xpath   //input[@id="CatlogValueincltesla"]
	howmanyKilometerText xpath   //*[@id="kmdrivediv"]//p
	kilometerTextBox     xpath   //input[@id="kmdrive"]
	continueButton       xpath   //button[@class='button-continue']
	vehicleDetailsText   xpath   //div[@class='vehicle-details']
	manufacturedDateText    xpath   //*[@id="Mfgmonthdiv"]//p[@class='vehicle-label']
	monthTextBox         xpath   //select[@id="Mfgmonth"]
	yearTextBox          xpath   //input[@id="Mfyear"]
	teslaModelText       xpath   //*[@id="teslamodeldiv"]//p
	teslaModelButton     xpath   //*[@id="teslamodeldiv"]/div[2]//fieldset
	modelSButton         xpath   //input[@id='ModelS']
	modelXLabel          xpath   //label[@id='ModelX']
	vehicleTrimLabel     xpath   //*[@id="VehicleTrimdiv"]//p[@class='vehicle-label']
	vechicleTrimTextBox  xpath   //select[@id="VehicleTrim"]
	backButton           xpath   //img[@class='img-back']
	allRightsLink        xpath   //div[@class='footer']//li[@class='nl-footer-item'][1]
	privacyInfoLink      xpath   //div[@class='footer']//li[@class='nl-footer-item'][2]
	conditionLink        xpath   //div[@class='footer']//li[@class='nl-footer-item'][3]
	aboutMarshLink       xpath   //div[@class='footer']//li[@class='nl-footer-item'][4]
	contactLink          xpath   //div[@class='footer']//li[@class='nl-footer-item'][5]
	netherlandLink       xpath   //div[@class='footer']//li[@class='nl-footer-item'][6]
	footer               xpath   //div[@class='footer']//ul[@class='nl-footer-list']
	header               xpath   /html/body/app-root/app-nl-header/nav
	mainContentBox       xpath   //div[@class='container-fluid driver']



= Main section =

  @on *
  backButton:
     height 22px
	 width 49px
	 css color is "#5C5C5C"
	 css font-family contains "Gotham"
	 css font-size is "20px"
	 css line-height is "24px"

  please-take-a-moment:
	 height 50px
	 width 744px
	 css color is "#5C5C5C"
	 css font-family contains "Gotham Light"
	 css font-size is "30px"
	 css line-height is "50px"
	 css text-align is "center"

  manufacturedDateText:
	 height 22px
	 width 325px
	 css color is "#5C5C5C"
	 css font-family is "Gotham"
	 css font-size is "20px"
	 css line-height is "24px"

  monthTextBox:
	 height 41px
	 width 105px
	 #border 1px solid #979797
	 css background-color is "#FFFFFF"

  yearTextBox:
	 height 41px
	 width 85px
	 #border 1px solid #979797
	 css background-color is "#FFFFFF"

  teslaModelText:
	 height 22px
	 width 115px
	 css color is "#5C5C5C"
	 css font-family is "Gotham"
	 css font-size is "20px"
	 css line-height is "24px"

  teslaModelButton:
	 height 57px
	 width 393px
	 #border 1px solid #979797
	 css border-radius is "28.5px"
	 css background-color is "#E9EAEC"

  modelSButton:
	 height 39px
	 width 122.24px
	 css border-radius is "19.5px"
	 css background-color is "#0090FF"

  modelXLabel:
	 height 18px
	 width 81.83px
	 css color is "#5C5C5C"
	 css font-family is "Gotham Light"
	 css font-size is "20px"
	 css line-height is "19px"

  doesYourTeslaText:
     height 22px
	 width 397px
	 css color is "#5C5C5C"
	 css font-family is "Gotham"
	 css font-size is "20px"

  yesNoButtonForAutoPilot:
	 height 57px
	 width 393px
	# border 1px solid #979797
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
	  #border 1px solid #979797
	  css border-radius is "28.5px"
	  css background-color is "#E9EAEC"

  personalButton:
	  height 39px
	  width 159px
	  css border-radius is "19.5px"
	  css background-color is "#0090FF"

  businessButton:
	  height 18px
	  width 86px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  #businessUseTypeText:
 	#  height 22px
	 # width 314px
	 # css color is "#CC0000"
	 # css font-family is "Gotham"
	 # css font-size is "20px"
	 # css line-height is "24px"

  businessUseTypeButton:
	  height 57px
	  width 1062px
	  #border 1px solid #979797
	  css border-radius is "28.5px"
	  css background-color is "#E9EAEC"

  rentalCarText:
	  height 18px
	  width 104px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  taxiLabel:
	  height 18px
	  width 41px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  drivingLabel,securityLabel:
	  height 18px
	  width 81px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  emergencyText:
	  height 18px
	  width 173px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  otherButton:
	  height 39px
	  width 121px
	  css border-radius is "19.5px"
	  css background-color is "#0090FF"

  includeExcludeTaxLabel:
	  height 22px
	  width 534px
	  css color is "#CC0000"
	  css font-family is "Gotham"
	  css font-size is "20px"
	  css line-height is "24px"

  includeExcludeButton:
	  height 57px
	  width 393px
	  #border 1px solid #979797
	  css border-radius is "28.5px"
	  css background-color is "#E9EAEC"

  includeButton:
	  height 39px
	  width 159px
	  css border-radius is "19.5px"
	  css background-color is "#0090FF"

  #includeLabel
	  #height 23px
	  #width 75px
	  #color #FFFFFF
	  #font-family Gotham
	  #font-size 20px
	  #font-weight bold
	  #line-height 25px
	  #text-align center

  excludeLabel:
	  height 18px
	  width 79px
	  css color is "#5C5C5C"
	  css font-family is "Gotham Light"
	  css font-size is "20px"
	  css line-height is "19px"
	  css text-align is "center"

  catalogValueText:
	  height 22px
	  width 375px
	  css color is "#5C5C5C"
	  css font-family is "Gotham"
	  css font-size is "20px"
	  css line-height is "24px"

  catalogValueTextBox:
	  height 41px
	  width 178px
	  #border 1px solid #979797
	  css background-color is "#FFFFFF"

  howmanyKilometerText:
	  height 22px
	  width 440px
	  css color is "#666666"
	  css font-family is "Gotham"
	  css font-size is "20px"
	  css line-height is "24px"

  kilometerTextBox:
	  height 41px
	  width 178px
	  #border 1px solid #979797
	  css background-color is "#FFFFFF"

  continueButton:
	  height 50px
	  width 217px
	  css background-color is "#CC0000"

  allRightsLink:
	  height 14px
	  width 252px
	  css color is "#5C5C5C"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"

  privacyInfoLink:
	  height 14px
	  width 104px
	  css color is "#0090FF"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"

  conditionLink:
	  height 14px
	  width 59px
	  css color is "#0090FF"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"

  aboutMarshLink:
	  height 14px
	  width 70px
	  css color is "#0090FF"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"

  contactLink:
	  height 14px
	  width 70px
	  css color is "#0090FF"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"

  netherlandLink:
	  height 14px
	  width 70px
	  css color is "#0090FF"
	  css font-family is "Helvetica Neue"
	  css font-size is "12px"
	  css line-height is "14px"


  footer:
	  height 53px
	  width 1440px
	  css background-color is "#FFFFFF"

  header:
	  height 57px
	  width 1440px

  mainContentBox:
	  height 1327px
	  width 1303px
	  css background-color is "#FBFCFD"

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
	  #border 1px solid #979797
	  css background-color is "#FFFFFF"

  vehicleDetailsText:
	  height 33px
	  width 215px
	  css color is "#333333"
	  css font-family is "Gotham"
	  css font-size is "30px"
	  css line-height is "35px"