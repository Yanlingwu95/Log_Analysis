# Log Analysis

The project in Udacity's full stack web development nanodegree program.

### Project Overview



### How to Execute?

#### Pre-Requisites:

[Python3](https://www.python.org/download/releases/3.0/) - The code uses version 3.6.8. 

[Vagrant](https://www.vagrantup.com/) - The software that configures the VM and lets you share files between your host computer and the VM's filesystem. 

[VirtualBox](https://www.virtualbox.org/) - The software that actually runs the virtual machine. 

[Git](https://git-scm.com/) - An open source version control system. 

#### Set up the Project:

1. Install VirtualBox:  I used the Ubuntu 18.04, install VirtualBox using the Ubuntu Software Center directly. 
2. Install Vagrant:  Run `sudo apt install vagrant`at the terminal to install and verify vagrant installation by `vagrant --version`. 
3. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) VM configuration which can preconfigure vagrant settings. 
4. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database. 

#### Launching the Virtual Machine:

    1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
    2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
    3. Change directory to /vagrant and look around with `ls`.

#### Explore the dataset:

1. To load the database by `psql -d news -f newsdata.sql` , which can connect to database. 
2. To run the database type `psql -d news` . 
3. You must run the commands from the Create views section here to run the python program successfully.
4. The database includes three tables:
     * The authors table includes information about the authors of articles.
     * The articles table includes the articles themselves.
     * The log table includes one entry for each time a user has accessed the site.

#### Create the tables we need:

- Create view article_view_number using:

```
CREATE view article_view_number AS
SELECT title, author, COUNT(*) AS views
FROM articles, log
WHERE log.path LIKE CONCAT('%', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY views DESC;
```

| Column | Type    |
| :----- | :------ |
| title  | text    |
| author | text    |
| views  | Integer |

- Create view error_log using: 

``` 
SELECT date(log.time), ROUND(100.0*SUM(case log.status WHEN '200 OK' then 0 else 1 END)/COUNT(log.status), 2) AS Percent_Error
FROM log
GROUP BY date(log.time)
ORDER BY Percent_Error DESC;
```

| Column        | Type  |
| :------------ | :---- |
| date          | date  |
| Percent Error | float |

#### Run the queries:

- From the vagrant directory inside the virtual machine,run logs.py using: 

```
python log.py
```

