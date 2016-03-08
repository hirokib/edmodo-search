drop table if exists products;
drop table if exists _source;
drop table if exists owner;
drop table if exists searchRatings;

create table products (
  _id integer primary key autoincrement,
  _index varchar(50) default '',
  _score double default 0.0,
  _type varchar(50) default ''
);


create table _source (
  product_id integer not null,
  title varchar(100) default '',
  min_price real not null default 0.0,
  long_desc text default "",
  nor_avg_rating real not null default 0.0,
  num_raters integer not null default 0,
  price real not null default 0.0,
  usage_rights integer,
  currency varchar(50) default '',
  owner integer not null,
  edm_score real not null default 0.0,
  content_type integer,
  is_shared boolean,
  url text not null default "",
  long_desc_html text not null default "",
  liked boolean,
  img_path text not null default "",
  nor_num_raters real not null default 0.0,
  creation_date datetime,
  img_has_other_size boolean,
  greads_review_url text not null default "",
  foreign key (product_id) references products(_id),
  foreign key (owner) references owner(id)
);

create table owner (
  id integer primary key autoincrement,
  thumb_url text not null default "",
  district_id integer,
  first_name text not null default "",
  type text not null default "",
  store_url text not null default "",
  followers integer not null default 0,
  last_name text not null default "",
  edmodo_url text not null default "",
  school_id integer
);

create table searchRatings (
	query	not null,
	product_id	integer not null,
	inappropriate	 boolean   default 0,
	nothelpful	boolean   default 0,
	wrongtags	boolean   default 0,
	spam	boolean   default 0,
  foreign key (product_id) references products(_id)

);
