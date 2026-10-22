Method: Install Jenkins Directly (No Key Needed)

Step 1: First, clean up the broken repository entries:

bash
sudo rm -f /etc/apt/sources.list.d/jenkins.list
sudo apt-key del "$(sudo apt-key list 2>/dev/null | grep -B1 jenkins | head -1 | awk '{print $NF}')" 2>/dev/null
sudo apt update

(Don't worry if the second command shows an error — that's fine.)

Step 2: Make sure Java is installed:

bash
java -version

If it's not installed:

bash
sudo apt install openjdk-17-jdk -y

Step 3: Download the Jenkins WAR file:

bash
wget https://get.jenkins.io/war-stable/latest/jenkins.war

This downloads Jenkins as a single file — no repository or key needed.

Step 4: Run Jenkins:

bash
java -jar jenkins.war

What you should see: A lot of text scrolling, and near the end:

*************************************************************
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:
a1b2c3d4e5f6789...
This may also be found at: /home/labuser/.jenkins/secrets/initialAdminPassword
*************************************************************
Jenkins is fully up and running

Step 5: Open your browser and go to:

http://localhost:8080

You should see the "Unlock Jenkins" page. Paste the password from the terminal output.





sudo apt install openjdk-21-jdk -y

  

If that doesn't find the package (Ubuntu 20.04 may not have Java 21 in its default repos), run this instead:


  
bash
sudo add-apt-repository ppa:openjdk-r/ppa -y
sudo apt update
sudo apt install openjdk-21-jdk -y

  
Step 2: Verify

  
bash
java -version

  

You should see something like:


  
openjdk version "21.0.x"

  
Step 3: Now run Jenkins

  
bash
java -jar jenkins.war
