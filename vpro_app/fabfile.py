from fabric.api import *
env.hosts='127.0.0.1'
env.user='vagrant'
env.password='vagrant'

def if_condition():
    if sudo("uname -a | awk '{print $4}' | cut -b 5-10") == "ubuntu":
       print "THIS IS UBUNTU SERVER"
       ubuntu()
    else:
       print "THIS IS CENTOS SERVER" 
       centos()

   
def ubuntu():
    ciserver_u


def centos():
    ci_c()
    app_c()
    db_c()
    lb_c()
    memchace_c()
    rabbitmq_c()
######################################### 

def ciserver_u():
     sudo("apt-get update -y")
     sudo("add-apt-repository ppa:openjdk-r/ppa -y")
     #sudo("apt-get install java* -y")
     sudo("apt-get update")
     sudo("apt-get install openjdk-8-jdk -y ")
     sudo("apt-get  install git -y")
     with cd("/"):
         sudo("git clone -b vp-memcached-rabbitmq https://github.com/wkhanvisualpathit/VProfile.git")
         sudo("apt-get install maven -y")
     with cd("//VProfile"):
         sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
         sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
         sudo("sed -i 's/localhost:3306/db01.com:3306/' src/main/resources/application.properties")
         sudo("sed -i 's/address=127.0.0.1/address='rmq011.com'/' src/main/resources/application.properties")
         sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache01.com'/' src/main/resources/application.properties")
         sudo("mvn clean install")


def ci_c():
     sudo("yum update -y")
     sudo("yum install epel-release -y")
     sudo("yum install  java-1.8.0-openjdk-devel.x86_64 -y")
     sudo("yum  install git -y")
     sudo("yum update -y")

     with cd("/root"):
         sudo("git clone -b vp-rem https://github.com/wkhanvisualpathit/VProfile.git")
         sudo("chmod +x maven.sh")
         #sudo("./maven.sh")
         sudo("mvn -version")
     with cd("/root/VProfile"):
          sudo("sed -i 's/password=password/password=root/g' src/main/resources/application.properties")
          sudo("sed -i 's/newuser/root/g' src/main/resources/application.properties")
          sudo("sed -i 's/localhost:3306/db01.com:3306/' src/main/resources/application.properties")
          sudo("sed -i 's/address=127.0.0.1/address='rmq01.com'/' src/main/resources/application.properties")
          sudo("sed -i 's/active.host=127.0.0.1/active.host='memcache01.com'/' src/main/resources/application.properties")
          sudo("mvn clean install")



def app_c():
     sudo("yum update -y")
     sudo("yum install  java-1.8.0-openjdk -y")
     sudo("yum install wget -y")
     with cd("/root"):
         sudo("wget http://redrockdigimark.com/apachemirror/tomcat/tomcat-8/v8.5.32/bin/apache-tomcat-8.5.32.tar.gz")
         sudo("mv apache-tomcat-8.5.32.tar.gz /opt/apache-tomcat-8.5.32.tar.gz")
     with cd("/opt"):
          sudo("tar -xvzf apache-tomcat-8.5.32.tar.gz")
          sudo("rm -rf /opt/apache-tomcat-8.5.32/webapps/ROOT")
          sudo("cp /root/VProfile/target/vprofile-v1.war /opt/apache-tomcat-8.5.32/webapps/ROOT.war")
          sudo("service iptables stop")
          sudo("chkconfig iptables off")
          sudo("nohup /opt/apache-tomcat-8.5.32/bin/startup.sh &")


def db_c():
     sudo("yum install epel-release -y")
     sudo("yum install mysql-server -y")
     sudo("service mysqld start")
     sudo("echo \"bind-address  = 0.0.0.0\" >> /etc/my.cnf ")
     #sudo("mysql -u root -e \"CREATE DATABASE accounts\" --password='';")
     sudo ("mysql -u root -e \"grant all privileges on *.* TO 'root'@'app01.com' identified by 'root'\" --password='';")
     #sudo("mysql -u root -e \"create user 'admin'@'%' identified by 'admin'\" --password='';")
     #sudo("mysql -u root -e \"GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%'\" --password='';")
     sudo("mysql -u root --password='' accounts < /root/VProfile/src/main/resources/db_backup.sql;")
     sudo("mysql -u root -e \"FLUSH PRIVILEGES\" --password='';")
     sudo("echo ")
     sudo("service mysqld restart")

    
    
def lb_c():
     sudo("yum install epel-release -y")
     sudo("yum install nginx -y")
     sudo("cat /vagrant/vproapp  > /etc/nginx/conf.d/vproapp.conf")
     sudo("systemctl stop firewalld")
     sudo("service nginx start")


def memcache_c():
    sudo("yum install memcached -y")
    sudo("memcached -p 11111 -U 11111 -u memcache -d")


#def rabbitmq_c():
#     sudo("yum update -y")
#    sudo("yum install wget -y")
#     sudo("yum install epel-release -y")
#     sudo("wget https://github.com/rabbitmq/erlang-rpm/releases/download/v19.3.6.8/erlang-19.3.6.8-1.e16.x86_64.rpm")
#     sudo("rpm -ivh erlang-19.3.6.8-1.e16.x86_64.rpm")
#     sudo("yum install socat -y")
#     sudo("wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-server-3.6.9.el6.noarch.rpm")
#     sudo("rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc")
#     sudo("yum update -y")
#     sudo("rpm -ivh rabbitmq-server-3.6.9-1.noarch.rpm")
#     sudo("service rabbitmq-server start")
#     sudo("service rabbitmq-server status")
     #sudo("rpm --import https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc")
     #sudo("yum update -y")
     #sudo("echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list")
     #sudo("wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -")
     #sudo("wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc| sudo apt-key add -")
     #sudo("yum install rabbitmq-server -y")
#     sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
#     sudo("rabbitmqctl add_user test test")
#     sudo("rabbitmqctl set_user_tags test administrator")


def rabbitmq_c():
    sudo("yum install epel-release -y")
    sudo("yum install wget -y")
    sudo("wget https://github.com/rabbitmq/erlang-rpm/releases/download/v19.3.6.8/erlang-19.3.6.8-1.el6.x86_64.rpm")
    sudo("rpm -ivh erlang-19.3.6.8-1.el6.x86_64.rpm")
    sudo("yum install socat -y")
    sudo("wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-server-3.6.9-1.el6.noarch.rpm")
# sudo   wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.9/rabbitmq-server-3.6.9-1.el6.noarch.rpm
    sudo("rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc")
#sudo yum install rabbitmq-server-3.6.9-1.noarch.rpm
    sudo("yum update")
#yum install rabbitmq-server-3.6.9-1.noarch.rpm
    sudo("rpm -ivh rabbitmq-server-3.6.9-1.el6.noarch.rpm")
    sudo("service rabbitmq-server start")
    sudo("service rabbitmq-server status")
    sudo("echo '[{rabbit, [{loopback_users, []}]}].' > /etc/rabbitmq/rabbitmq.config")
    sudo("rabbitmqctl add_user test test")
    sudo("rabbitmqctl set_user_tags test administrator")
