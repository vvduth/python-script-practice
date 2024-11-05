from  fabric.api import *

def greeting(msg):
    print("Good {}".format(msg))

def system_info():
    print("Disk Space")
    local("df -h")

    print("RAM size")
    local("free -m")


def remote_exec():
    print("Get system info")
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")

    sudo("yum install mariadb-server -y")
    sudo("systemctl start mariadb")
    sudo("systemctl enable mariadb")

def web_setup(weburl, dirname):
    print("#############################################")
    local("apt install zip unzip -y")
    print("#############################################")
    print("Installing dependencies")
    sudo("yum install httpd wget unzip -y")

    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    local(("wget -O website.zip %s") % weburl)
    local("unzip -o website.zip")

    with lcd(dirname):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html",use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip tooplate.zip")
    sudo("systemctl restart httpd")

    print("Done bro.")

