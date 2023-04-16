if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TECHNICAL-RB/Autofilter-bot-cynite.git /Autofilter-bot-cynite
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Autofilter-bot-cynite
fi
cd /Autofilter-bot-cynite
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
