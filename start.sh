if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Rishi09090909/Autofilterbot-.git /Autofilterbot-
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Autofilterbot-
fi
cd /Autofilterbot-
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
