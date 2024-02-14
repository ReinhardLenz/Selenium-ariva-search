class Locators():
    # Login page objects
    cookie_acceptor= ".js-bsg-cookie-layer__confirm > span:nth-child(1)"
    cookie_acceptor_class="message-component message-button no-children focusable sp_choice_type_11 first-focusable-el"
    cookie_acceptor_frame_id="sp_message_iframe_851110"
    cookie_acceptor_button_class="message-component message-button no-children focusable sp_choice_type_11 first-focusable-el"
    cookie_acceptor_button_title="Akzeptieren und weiter"
    cookie_acceptor__inner_iframe_full_xpath="/html/body/div[7]/iframe"
    cookie_acceptor__inner_iframe_xpath='//*[@id="sp_message_iframe_851110"]'
    Rendite_von_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[3]/tbody/tr[1]/td[2]/input"
    Rendite_bis_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[3]/tbody/tr[1]/td[3]/input"
    Suchen_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/div/input"
    Coupontyp_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[2]/tbody/tr[2]/td[2]/select"
    Anleihetype_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[2]/tbody/tr[1]/td[2]/select"
    #* *  * *
    
    cookie_acceptor__outer_iframe_full_xpath="/html/body/iframe"
    cookie_acceptor_full_XP="/html/body/div/div[2]/div[3]/div[1]/div[3]/div/button"
    Anleihentyp_full_XPath="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[1]/tbody/tr[2]/td[2]/select"
    Waehrung_select_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[2]/tbody/tr[3]/td[2]/select"
    Restlaufzeit_start_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[2]/tbody/tr[5]/td[2]/select"
    Restlaufzeit_end_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[3]/form/table[2]/tbody/tr[5]/td[3]/select"
    Unternehmensanleihe_button_full_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/div[1]/div[3]/div/div[1]/div[1]/a[3]"
    Low_coupon_button_XPATH="//*[@id='pageAnleihen']/div[1]/div[3]/div/div[1]/div[2]/a[2]"
    Low_coupon_button_full_XPATH="/html/body/div[1]/div[3]/div[9]/div[3]/div[1]/div[3]/div/div[1]/div[2]/a[2]"

    Refine_search_under_low_coupon_selection_XPATH="//*[@id='CONTENT']/div[3]/a"



    Refine_search_under_low_coupon_selection_CSS_selector="#CONTENT > div:nth-child(3) > a"

    Refine_search_under_low_coupon_selection_Select_currency_XPATH="//*[@id='typCurrency']"
    #miksi menee
    Refine_search_under_low_coupon_selection_Select_currency_full_XPATH="/html/body/div[1]/div[3]/div[9]/div[3]/div[3]/form/table[2]/tbody/tr[3]/td[2]/select"
    
    Refine_search_under_low_coupon_Rendite_low_ID="minRendite"
    Refine_search_under_low_coupon_Rendite_low_XPATH="//*[@id='minRendite']"
    Refine_search_under_low_coupon_Rendite_high_ID="maxRendite"
    Refine_search_under_low_coupon_Rendite_high_XPATH="//*[@id='maxRendite']"
    Refine_search_under_low_coupon_Kupon_high_ID="maxKupon"
    Refine_search_under_low_coupon_Kupon_high_XPATH="//*[@id='maxKupon']"
    Refine_search_Kupon_type_ID="typKupon"
    Refine_search_Kupon_type_XPATH="//*[@id='typKupon']"
    Refine_Search_min_duration_ID="minRLZ"
    Refine_Search_min_duration_XPATH="//*[@id='minRLZ']"
    Refine_Search_max_duration_ID="maxRLZ"
    Refine_Search_max_duration_XPATH="//*[@id='maxRLZ']"
    Refine_Search_click_Search_button_XPATH="//*[@id='CONTENT']/div[3]/div[3]/form/div/input"
    Refine_Search_type_bond_ID="typAnleihe"
    Refine_Search_type_bond_XPATH="//*[@id='typAnleihe']"

    Refine_search_under_low_coupon_selection_full_XPATH="/html/body/div[1]/div[3]/div[9]/div[3]/a"
    Suche_weiter_bearbeiten_XPATH="/html/body/div[1]/div[3]/div[9]/div[4]/a"
    Wahrung_click_id="bsg-filters-btn-bgs-filter-7"
    Wahrung_click_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[6]/div/button"
    Wahrung_click_new_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[6]/div/div/div/div[1]/div/div[1]/ul/li[3]/div/div/input"
    Wahrung_click_new_ID="bsg-checkbox-1576"
    Wahrung_write_field_css="#bsg-filters-menu-bgs-filter-7 > div > div.bsg-dropdown__search > div > input"
    Wahrung_write_field_full_xp="/html/body/main/div[2]/div/div/div/form/div/div[2]/ul/li[7]/div/button"
    Wahrung_write_field_simpl_xp="//*[@id='bsg-filters-btn-bgs-filter-7']"
    Wahrung_checkbox_css="#bsg-checkbox-1571"
    Wahrung_checkbox_Euro_id="bsg-checkbox-1569"
    Wahrung_checkbox_Euro_full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[6]/div/div/div/div[2]/div/div[1]/ul/li/div/div/label"
    #Wahrung_checkbox_Euro_Xpath="//*[@id="mCSB_4_container"]/ul/li/div/div/label"
    Wahrung_checkbox_Euro_full_Xpath="/html/body/main/div[2]/div/div/div/form/div/div[2]/ul/li[6]/div/div/div/div[2]/div/div[1]/ul/li/div/div/label"
    Wahrung_anwenden_css="#bsg-filters-menu-bgs-filter-7 > div > div.bsg-dropdown__footer > button"
    Zusatzliche_Filter_Textfield_Wahrung_Full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[6]/div/div/div/div[1]/div/input"

    #Zusatzliche_Filter_css="#bsg-filters-btn-bgs-filter-8"
    Zusatzliche_Filter_css="#bsg-filters-btn-bgs-filter-11"
    handelbare_Einh_css="html.tablesaw-enhanced body.bsg-page main.bsg-main.bsg-page__main div.bsg-searchlist div.bsg-searchlist__header.bsg-ribbon.bsg-theme--cira div.bsg-container div.bsg-row.bsg-ribbon__row form.bsg-searchlist__form.js-bsg-searchlist div.bsg-searchlist__form-items-wrapper div.bsg-searchlist__dynamic-filters ul.bsg-filter-group li.bsg-filter-group__item.bsg-filter-group__item--fluid div.bsg-dropdown.bsg-dropdown--gina.bsg-filter.js-bsg-filter div#bsg-filters-menu-bgs-filter-8.bsg-dropdown__menu.bsg-filter__panel.bsg-filter__panel--gina div.bsg-dropdown__block div.bsg-scrollbox.js-bsg-scrollbox.bsg-dropdown__scrollbox.mCustomScrollbar._mCS_5 div#mCSB_5.mCustomScrollBox.mCS-bsg-dropdown-default.mCSB_vertical.mCSB_inside div#mCSB_5_container.mCSB_container ul.bsg-dropdown__list.bsg-dropdown__list--shorten li.bsg-dropdown__item div.bsg-form-controlbox.bsg-form-controlbox--custom.bsg-form-controlbox--leia div input#bsg-checkbox-11.bsg-form-controlbox__control"
    #new 2023
    Handelbare_einh_Button_full_xpath="/html/body/main/div[2]/div/div/div/form/div/div[3]/ul/li/div/div/div/div[2]/div/div[1]/ul/li[3]/div/div/input"
    Handelbare_einh_Button_xpath="//*[@id='bsg-checkbox-14']"
    Handelbare_einh_Button_id="bsg-checkbox-14"
    Handelbare_einh_Button_class_1="bsg-form-controlbox__control"
    
    Zusatzliche_Filter_Textfield_Full_XPath="/html/body/main/div[2]/div/div/div/form/div/div[3]/ul/li/div/div/div/div[1]/div/input"
    Zusatzliche_Filter_Anwenden_Full_XPath="/html/body/main/div[2]/div/div/div/form/div/div[3]/ul/li/div/div/div/div[3]/button"
    Zusatzliche_Filter_Full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[3]/ul/li/div/button"
    
    
    Handelbare_Einheit_class="bsg-btn bsg-btn--dropdown bsg-btn--nhs bsg-dropdown__btn bsg-filter__control bsg-filter__control--juna"
    Anwenden_button_css="#bsg-filters-menu-bgs-filter-8 > div > div.bsg-dropdown__footer > button"
    Handelbare_einh_Button_class='bsg-btn bsg-btn--dropdown bsg-btn--nhs bsg-dropdown__btn bsg-filter__control bsg-filter__control--juna'
    Handelbare_einh_Button_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[7]/div/button"
    right_arrow_full_xp="/html/body/main/div[2]/div[3]/div/div/div[1]/div/div[1]/a[2]"
    right_arrow_class="btn tablesaw-nav-btn tablesaw-btn btn-micro right"

    min_Littera_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[7]/div/div/div/div[2]/div[1]/input"
    max_Littera_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[7]/div/div/div/div[2]/div[2]/input"
    Anwenden_littera_xp ="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[7]/div/div/div/div[4]/button"
    Anwenden_littera_css="#bsg-filters-menu-bgs-range-filter-1594 > div > div.bsg-dropdown__footer > button"

    Delete_littera_full_Xpath="/html/body/main/div[2]/div[2]/div/div/ul/li/button"
    #                          /html/body/main/div[2]/div[2]/div/div/ul/li/button
    # not successful:
    Anwenden_littera_class="bsg-btn bsg-btn--juna bsg-btn--nes bsg-btn--centered bsg-dropdown__btn-apply"
   # Anwenden_littera_full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[7]/div/div/div/div[4]/button"
    Anwenden_littera_full_XPath="/html/body/main/div[2]/div/div/div/form/div/div[2]/ul/li[7]/div/div/div/div[4]/button"
    
    Falligkeit_click_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[4]/div/button"
    Smaller_date_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[4]/div/div/div/div[2]/div[1]/input"

    Smaller_date_ID="bsg-date-range-input-1623"
    Bigger_date_xp= "/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[4]/div/div/div/div[2]/div[2]/label"
    Bigger_date_2_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[4]/div/div/div/div[2]/div[2]/input"
    Anwenden_Falligkeit_full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[4]/div/div/div/div[4]/button"
    Rendite_button_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[5]/div/button"
    Rendite_lower_margin_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[5]/div/div/div/div[2]/div[1]/input"
    Rendite_upper_margin_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[5]/div/div/div/div[2]/div[2]/input"
    Rendite_anwenden_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[5]/div/div/div/div[4]/button"
    Weitere_Treffer_anzeigen_xp="/html/body/main/div[2]/div[3]/div/div/div[2]/button"
    

    Eur_chip_close_full_xp="/html/body/main/div[2]/div[2]/div/div/ul/li[2]/button/span[2]/svg/use//svg/path[2]"
    Eur_chip_close_id="outline-close-24px"
    Eur_chip_close_selector="#outline-close-24px > path:nth-child(2)"

    Rendite_sort_full_xp="/html/body/main/div[2]/div[3]/div/div/div[1]/table/thead/tr/th[5]/button"
    
    Gelisteter_Zeitraum_preselector_Button_id="bsg-checkbox-1612"
    Gelisteter_Zeitraum_Button_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[8]/div/button"
    Gelisteter_Zeitraum_smaller_date_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[8]/div/div/div/div[2]/div[1]/input"
                                         
    Gelisteter_Zeitraum_smaller_date_ID="Gelisteter_Zeitraum_smaller_date_ID"
    Gelisteter_Zeitraum_Bigger_date_xp="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[8]/div/div/div/div[2]/div[2]/input"
    Anwenden_Gelisteter_Zeitraum_full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[8]/div/div/div/div[4]/button"
    
    #For Type of Bond
    Preselector_Anleihen_Typ_ID="bsg-filters-btn-bgs-filter-3"
    Preselector_Anleihen_Typ_Full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[2]/div/button"
    Select_Unternehmensanleihe_Checkbox_FullXPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[2]/div/div/div/div[1]/div/div[1]/ul/li[4]/div/div/input"
    Select_Unternehmensanleihe_Checkbox_ID="bsg-checkbox-1536"
    Anwenden_Unternehmensanleihe_Select_full_XPath="/html/body/main/div[2]/div[1]/div/div/form/div/div[2]/ul/li[2]/div/div/div/div[2]/button"
    Anwenden_Unternehmensanleihe_Select_class="bsg-btn bsg-btn--juna bsg-btn--nes bsg-btn--centered bsg-dropdown__btn-apply js-bsg-filter__closer"
    


