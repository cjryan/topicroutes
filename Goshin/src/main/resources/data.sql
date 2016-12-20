INSERT INTO question (question, timestamp) VALUES ('Are Cookies Delicious?', '2016-12-26 20:00:00')
INSERT INTO question (question, timestamp) VALUES ('What is the average speed velocity of a swallow?', '1974-06-13 20:00:00')
INSERT INTO question (question, timestamp) VALUES ('What is a reasonable way to store graph data in a relational database?', '2016-12-19')

INSERT INTO note (note, question_id) VALUES ('Cookies are probably very delicious', 1) 
INSERT INTO note (note, question_id) VALUES ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ultricies tellus ut porta lobortis. Aliquam erat volutpat. Ut eget elit eros. Quisque dignissim velit quis mollis rhoncus. Praesent congue urna ut tristique gravida. Praesent ornare eros eget tortor pellentesque imperdiet. Cras condimentum dui id quam congue faucibus. Nunc malesuada augue vestibulum, consequat tortor in, sollicitudin tellus. ', 1)

INSERT INTO reference (title, the_abstract, question_id) VALUES ('Wikipedia :: Cookies and Taste', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ultricies tellus ut porta lobortis. Aliquam erat volutpat. Ut eget elit eros. Quisque dignissim velit quis mollis rhoncus. Praesent congue urna ut tristique gravida. Praesent ornare eros eget tortor pellentesque imperdiet. Cras condimentum dui id quam congue faucibus. Nunc malesuada augue vestibulum, consequat tortor in, sollicitudin tellus. ', 1)

INSERT INTO tag (tag) VALUES ('edible')
INSERT INTO tag (tag) VALUES ('frustrating')

INSERT INTO note_tag (note_id, tag_id) VALUES (1, 1)
INSERT INTO note_tag (note_id, tag_id) VALUES (2, 1)
