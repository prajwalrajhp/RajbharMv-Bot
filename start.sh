if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/CrezyDeveloper143/Autofilterbot-.git /Autofilterbot-
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Auto-Filter-V5
fi
cd /Autofilterbot-
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
