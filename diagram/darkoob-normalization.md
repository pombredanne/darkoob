Darkoob DataBase Normalization Diagram
======================================
At first step we should specific all data and first's plan of tables and all functional dependence.

Preliminary Tables
------------------

### Table1


    -----------------------------------------------------------------------------------------------------------------
    |         |           |       |      |       |      |      |        |          |           |          |         |
    |         V           V       V      V       V      V      V        V          V           V          V         V
-----------------------------------------------------------------------------------------------------------------------------
|user_name|first_name|last_name|email|password|gender|mobile|city_id|city_name|country_id|country_name|school_id|school_name|
-----------------------------------------------------------------------------------------------------------------------------
                                                               |         ^         ^  |        ^  ^         |         ^
							       |         |         |  |        |  |         |         |
							       ---------------------------------  |         -----------
                                                                                      |           |
                                                                                      -------------
	1.user_name -> Table1
	2.city_id -> city_name, country_id, country_name 
	3.country_id -> country_name 
	4.school_id -> school_name


### Table2



              -----------------------------------                -------------------------------
              |        |         |              |                |          |                  |
              |        V         V              V                |          V                  V
----------------------------------------------------------------------------------------------------------
|user_name|post_id|post_title|post_text|post_submitted_time|comment_id|comment_text|submited_comment_time|
----------------------------------------------------------------------------------------------------------
     |        |                                                  ^            ^                ^
     |        |                                                  |            |                |
     -------------------------------------------------------------------------------------------


### Table3



    -----------------------------------------------------------------------------------------------------------------------------------------------------------
    |       |            |              |            |          |            |           |          |            |              |             |       |       |
    |       V            V              V            V          V            V           V          V            V              V             V       V       V
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
|book_id|book_title|publisher_id|publisher_name|language_id|language_name|author_id|author_name|author_rate|translator_id|translator_name|book_rate|tag_id|tag_name|
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
                          |            ^              |           ^           |           ^          ^            |              ^                     |      ^
                          |            |              |           |           |           |          |            |              |                     |      |
                          --------------              -------------           ------------------------            ----------------                     --------


### Table4    
              ------------------------------------------------------
              |                                                    V
--------------------------------------------------------------------------
|user_name|book_id|review_text|review_rate|review_submited_time|review_id|
--------------------------------------------------------------------------
     ^         ^          ^           ^              ^              |
     |         |          |           |              |              |
     ----------------------------------------------------------------


### Table5


     --------------------------------------------
     |              |               |           |
     |              V               V           V
---------------------------------------------------------
|user_name|followed_user_name|followed_date|followship_id|
---------------------------------------------------------
                    ^               ^            |
                    |               |            |
                    ------------------------------


All field's are atomic and in one normal form.

Normalization of Table1
-----------------------

	user_name is a condidate key, In second normal form we should remove all partial dependancy. There are not exisits any partial dependancy in Table1 so Table1 is in second normal form.
	In third normal forms we should remove all transitive dependance.
	 
	
### Table1.1

    ---------------------------------------------------------------------
    |         |           |       |      |       |      |      |        | 
    |         V           V       V      V       V      V      V        V       
-------------------------------------------------------------------------------
|user_name|first_name|last_name|email|password|gender|mobile|city_id|school_id|
-------------------------------------------------------------------------------

	This table is BC normal form(BCNF).
	This table has multi-value dependency in mobile and school_id, so we should correction our table's:

	#### Table1.1.1
	    -----------
	    |         |
	    |         V
	------------------
	|user_name|mobile|
	------------------

	#### Table1.1.2
	     -----------
	     |         |
	     |         V
	---------------------
	|user_name|school_id|
	---------------------

	#### Table1.1.3

	    ------------------------------------------------------
	    |         |           |       |      |       |       |              
	    |         V           V       V      V       V       V                   
	--------------------------------------------------------------
	|user_name|first_name|last_name|email|password|gender|city_id|
	--------------------------------------------------------------


### Table1.2

-----------------------
|school_id|school_name|
-----------------------
     |         ^
     |         |
     -----------

This table is BCNF 

### Table1.3

------------------------------
|city_id|city_name|country_id|
------------------------------
   |         ^         ^                 
   |         |         |                   
   --------------------- 

This table is BCNF 

### Table1.4

      ------------
      |          |
      |          V
-------------------------
|country_id|country_name|
-------------------------

This table is BCNF 

Normalization of Table2(in daghone:D)
-----------------------

    --------------------------------------------------
    |         |         |              |             |
    |         V         V              V             V
-----------------------------------------------------------
|post_id|post_title|post_text|post_submited_time|user_name|
-----------------------------------------------------------
   

    ------------------------------------------------
    |            |                 |               |           
    |            V                 V               V           
---------------------------------------------------------
|comment_id|comment_text|comment_submited_time|user_name|
---------------------------------------------------------

   -----------
   |         |
   |         V
--------------------
|post_id|comment_id|
--------------------


	(user_name, post_id) is a candidate key, for convert this table to second normal form we should remove all partial dependancy.

              -----------------------------------
              |        |         |              |
              |        V         V              V
----------------------------------------------------------------------------------------------------------
|user_name|post_id|post_title|post_text|post_submitted_time|comment_id|comment_text|submited_comment_time|
----------------------------------------------------------------------------------------------------------
     |        |                                                  ^            ^                ^
     |        |                                                  |            |                |
     -------------------------------------------------------------------------------------------
                          
Normalization of Table3
-----------------------
	book_id is condidate key of this table, In second normal form we should remove all transitive dependance. There are not exsists any transitive dependancy, so this table in second normal form.
	In third normal forms we should remove all transitive dependance.


### Table3.1

    ------------------------------------------------------------------------------
    |       |            |            |          |          |            |       |
    |       V            V            V          V          V            V       V  
--------------------------------------------------------------------------------------
|book_id|book_title|publisher_id|language_id|author_id|translator_id|book_rate|tag_id|
--------------------------------------------------------------------------------------

	We see Multi value dependency(MVD) in tag_id and author_id and translator_id, so we have modified:


	#### Table3.1.1

	    ----------------------------------------------
	    |       |            |            |          |         
	    |       V            V            V          V          
	-------------------------------------------------------
	|book_id|book_title|publisher_id|language_id|book_rate|
	-------------------------------------------------------


	#### Table3.1.2
	     --------
	     |      |
	     |      V
	-------------------
	|book_id|author_id|
	-------------------

	#### Table3.1.3
	     --------
	     |      |
	     |      V
	-----------------------
	|book_id|translator_id|
	-----------------------

	#### Table3.1.4
	     --------
	     |      |
	     |      V
	----------------
	|book_id|tag_id|
	----------------




### Table3.2

-----------------------------
|publisher_id|publisher_name|
-----------------------------
      |            ^              
      |            |    
      -------------- 

### Table3.3

---------------------------
|language_id|language_name|
---------------------------
      |            ^              
      |            |    
      --------------

### Table3.4 

-----------------------------------
|author_id|author_name|author_rate|
-----------------------------------
     |         ^            ^  
     |         |            |
     ------------------------

### Table3.5

-------------------------------
|translator_id|translator_name|
-------------------------------
      |              ^              
      |              |    
      ---------------- 

### Table3.6

-----------------
|tag_id|tag_name|
-----------------
   |       ^              
   |       |    
   --------- 

Normalization of Table4
-----------------------

	there is not exeist any partial dependency and transitive dependency, but this table isn't BCNF

### Table4.1 


    ---------
    |       |
    |       V
-------------------
|book_id|review_id|
-------------------


### Table4.2

------------------------------------------------------------------
|user_name|review_text|review_rate|review_submited_time|review_id|
------------------------------------------------------------------
     ^         ^          ^                   ^             |
     |         |          |                   |             |
     --------------------------------------------------------

Normalizattion of Table5
------------------------

	user_name is a condidate key for this table, and there are no exsist any partial depandency.
	for convert this table to third normal form we should remove all transitive dependancy.

### Table5.1
     --------------
     |            |   
     |            V   
-------------------------
|user_name|followship_id|
-------------------------


### Table5.2
------------------------------------------------
|followed_user_name|followed_date|followship_id|
------------------------------------------------
         ^               ^            |
         |               |            |
         ------------------------------


