@objects
    logo                               xpath     //*[@class="marshLogo"]
    separator_above                            xpath     //*[@class="marshSeparator"]
    copy_rights                          xpath     //*[@id="_footer"]/div[2]/span[1]
    Terms_of_use                         xpath     //*[@id="_footer"]/div[2]/span[3]/a[1]
    Privacy_policy                       xpath     //*[@id="_footer"]/div[2]/span[3]/a[2]
    Powered_by                           xpath     //*[@id="_footer"]/div[2]/span[2]
    separator_below                      xpath     //*[@id="_footer"]/div[1]

= Main section =
    @on *

    @on desktop
    copy_rights:
        aligned horizontally all Terms_of_use

    Terms_of_use:
        aligned horizontally all Privacy_policy
        text is "Terms Of Use"

    Privacy_policy:
        aligned horizontally all Powered_by
        text is "Privacy Policy"

    Powered_by:
        aligned horizontally all copy_rights
        text is "POWERED BY MARSH DIGITAL"

    @on tablet
    copy_rights:
        aligned horizontally all Terms_of_use

    Terms_of_use:
        aligned horizontally all Privacy_policy
        text is "Terms Of Use"

    Privacy_policy:
        aligned horizontally all Powered_by
        text is "Privacy Policy"

    Powered_by:
        aligned horizontally all copy_rights
        text is "POWERED BY MARSH DIGITAL"