create table users(
    id int primary key,
    name varchar(255),
    password varchar(255),
    data_query varchar(255) default '',
    type_query varchar(255) default ''
);

drop table users;
insert into users(id, name, password) values (0, 'root', 'root');

select * from users;