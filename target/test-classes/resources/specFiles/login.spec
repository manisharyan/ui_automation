@objects
    First_header			xpath 		//*[@id="allinone"]/main/section/div/div/h2
    logo 				    xpath 		//*[@id="mainNav"]/div/a/img
    main_page				xpath		//html
    Email_address_Text			css 		#logIn div:nth-child(2) div label
    Password_Text			xpath		//label[@for='pwdButton']
    Remember_Email_username_Text	xpath		//input[@name='rememberuser']//following-sibling::p
    Subheading				xpath		//h2[contains(text(),'Marsh')]//following-sibling::p
    Forgot_Password_Text		xpath		//a[contains(text(),'Forgot Password')]
    Text_before_login_Help		xpath		//*[@id="logIn"]/div[5]/div/p[contains(text(),'Marsh')]
    Email_address_Textbox		xpath	 	//*[@id='uidButton']
    Password_Textbox			xpath	 	//*[@id='pwdButton']
    Login_button			xpath		//*[@id='loginButton']
    Email_address_Asterick		xpath 		//label[@for='uidButton']//span


= Main section =
	First_header:
		text is "Marsh Login"
		css font-size is "42px"
		css text-align is "start"
		height 42px
		width 1140px

	logo:
		image file expectedImages/logo.png, error 5%
		height 61px
		width 174px

	main_page:
		image file expectedImages/fullPage.png, error 4%

	Email_address_Text:
		text is "EMAIL ADDRESS*"
		css font-size is "13px"
		css text-align is "left"
		height 15px
		width 568px

	Email_address_Asterick:
		text is "*"
		aligned horizontally top Email_address_Text 1px

	Password_Text:
		text is "PASSWORD"

	Remember_Email_username_Text:
		text is "REMEMBER MY EMAIL/USERNAME"

	Subheading:
		text is "The content you are about to view is secured. Please login for access."

	Forgot_Password_Text:
		text is "FORGOT PASSWORD?"

	Text_before_login_Help:
		text is "*MARSH COLLEAGUES, PLEASE LOGIN WITH YOUR NETWORK (OR MARSHPASS) ID. FOR QUESTIONS, PLEASE REVIEW THIS  LOGIN HELP ."

	Password_Textbox:
		css text-align is "start"


	Login_button:
		aligned vertically left Password_Textbox
		width 60px
		height 28px