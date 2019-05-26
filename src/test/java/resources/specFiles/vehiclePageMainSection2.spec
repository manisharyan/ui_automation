@objects
	businessUseTypeText  	xpath  //*[@id="BusinessUseTypediv"]/div[1]/p
    businessUseTypeButton 	xpath  //*[@id="BusinessUseTypediv"]/div[2]/div/fieldset
    rentalCarText         	xpath  //label[@id="RentalCar"]
    taxiLabel             	xpath  //label[@id="Taxi"]
    deliveryLabel         	xpath  //label[@id="Delivery"]
    securityLabel         	xpath  //label[@id="Security"]
    drivingLabel          	xpath  //label[@id="DrivingInstructor"]
    emergencyText         	xpath  //label[@id="EmergencyServices"]
    otherButton           	xpath  //input[@id="Other"]
    includeExcludeButton 	xpath  //*[@id="CatalogValueinclvatdiv"]/div[2]/div/fieldset
    includeButton         	xpath  //input[@id="Including"]
    excludeLabel          	xpath  //label[@id="Excluding"]
    includeExcludeTaxLabel 	xpath  //*[@id="CatalogValueinclvatdiv"]//p


= main section =

	@on *
	businessUseTypeText:
		height 22px
		width  314px
		css color is "#CC0000"
		css font-family contains "Gotham"
		css font-size is "20px"
		css line-height is "24px"

	businessUseTypeButton:
		height 57px
		width 1062px
		css border is "1px solid #979797"
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
		css border is "1px solid #979797"
		css border-radius is "28.5px"
		css background-color is "#E9EAEC"

	includeButton:
		height 39px
		width 159px
		css border-radius is "19.5px"
		css background-color is "#0090FF"

	excludeLabel:
		height 18px
		width 79px
		css color is "#5C5C5C"
		css font-family is "Gotham Light"
		css font-size is "20px"
		css line-height is "19px"
		css text-align is "center"

