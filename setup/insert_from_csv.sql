COPY badges(id,user_id,class,name,tag_based,date)
FROM 'D:\RawData\csv\Badges.csv' 
DELIMITER ',' 
CSV HEADER;

COPY comments(id,post_id,user_id,score,content_license,user_display_name,text,creation_date)
FROM 'D:\RawData\csv\Comments.csv' 
DELIMITER ',' 
CSV HEADER;

COPY post_history(id,post_id,user_id,post_history_type_id,user_display_name,content_license,revision_guid,text,comment,creation_date)
FROM 'D:\RawData\csv\PostHistory.csv' 
DELIMITER ',' 
CSV HEADER;

COPY post_links(id,related_post_id,post_id,link_type_id,creation_date)
FROM 'D:\RawData\csv\PostLinks.csv' 
DELIMITER ',' 
CSV HEADER;

COPY posts(id,owner_user_id,last_editor_user_id,post_type_id,accepted_answer_id,score,parent_id,view_count,answer_count,comment_count,owner_display_name,last_editor_display_name,title,tags,content_license,body,favorite_count,creation_date,community_owned_date,closed_date,last_edit_date,last_activity_date)
FROM 'D:\RawData\csv\Posts.csv' 
DELIMITER ',' 
CSV HEADER;

COPY tags(id,excerpt_post_id,wiki_post_id,tag_name,count)
FROM 'D:\RawData\csv\Tags.csv' 
DELIMITER ',' 
CSV HEADER;

COPY users(id,account_id,reputation,views,down_votes,up_votes,display_name,location,profile_image_url,website_url,about_me,creation_date,last_access_date)
FROM 'D:\RawData\csv\Users.csv' 
DELIMITER ',' 
CSV HEADER;

COPY votes(id,user_id,post_id,vote_type_id,bounty_amount,creation_date)
FROM 'D:\RawData\csv\Votes.csv' 
DELIMITER ',' 
CSV HEADER;