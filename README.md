FTB
======

Stuff for the FTB Wiki.

navitems.py
-----------
This will turn a list of names in work/navitem_input.txt to NI templates. It will ask you for the mod abbreviation for use with the tilesheet extension. For example, 'Item' with abbreviation 'EX' will become '   -->{{NI|Item|mod=EX}}{{,}}<.!--'. (no period between < and !) navitem_input.txt will not be replaced, instead out/navitem_output.txt will be created. 

main_page_list.py
-----------------
This will turn a list of names in the work/mainlist_input.txt to "formatted" wiki markup for the Mods and Minor Mods lists that go on the Main page. For example, 'Name' will become '[[Name]] {{*}} '. mainlist_input.txt will not be replaced, instead out/mainlist_output.txt will be created.