@objects
    catalogValueText      xpath   //*[@id="CatlogValueincltesladiv"]//p[@class='vehicle-label']
    catalogValueTextBox   xpath   //input[@id="CatlogValueincltesla"]
    howmanyKilometerText  xpath   //*[@id="kmdrivediv"]//p
    kilometerTextBox      xpath   //input[@id="kmdrive"]
    continueButton        xpath   //button[@class='button-continue']
    allRightsLink        xpath   //div[@class='footer']//li[@class='nl-footer-item'][1]
    privacyInfoLink      xpath   //div[@class='footer']//li[@class='nl-footer-item'][2]
    conditionLink        xpath   //div[@class='footer']//li[@class='nl-footer-item'][3]
    aboutMarshLink       xpath   //div[@class='footer']//li[@class='nl-footer-item'][4]
    contactLink          xpath   //div[@class='footer']//li[@class='nl-footer-item'][5]
    netherlandLink       xpath   //div[@class='footer']//li[@class='nl-footer-item'][6]
    footer               xpath   //div[@class='footer']//ul[@class='nl-footer-list']

= main section =

  @on *
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
	  css border is "1px solid #979797"
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
