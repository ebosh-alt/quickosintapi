create table users(
    id int primary key,
    name varchar(255),
    password varchar(255)
);

insert into users(id, name, password) values (1, 'root', 'root');

select * from users;