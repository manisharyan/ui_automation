@objects
    please-take-a-moment  xpath   //div[@class='please-take-a-moment']
    vehicleDetailsText    xpath   //div[@class='vehicle-details']
    manufacturedDateText  xpath   //*[@id="Mfgmonthdiv"]//p[@class='vehicle-label']
    monthTextBox          xpath   //select[@id="Mfgmonth"]
    yearTextBox           xpath   //input[@id="Mfyear"]
    teslaModelText        xpath   //*[@id="teslamodeldiv"]//p
    teslaModelButton      xpath   //*[@id="teslamodeldiv"]/div[2]//fieldset
    modelSButton          xpath   //input[@id='ModelS']
    modelXLabel           xpath   //label[@id='ModelX']
    backButton            xpath   //img[@class='img-back']
    header               xpath   /html/body/app-root/app-nl-header/nav



= section =

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

  vehicleDetailsText:
  	  height 33px
  	  width 215px
  	  css color is "#333333"
  	  css font-family is "Gotham"
  	  css font-size is "30px"
  	  css line-height is "35px"

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
     css border is "1px solid #979797"
     css background-color is "#FFFFFF"

  yearTextBox:
     height 41px
     width 85px
     css border is "1px solid #979797"
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

  header:
	  height 57px
	  width 1440px
