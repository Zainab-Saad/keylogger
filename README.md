chmod +x install_db.sh
./install_db.sh
chmod +x code_runner.sh
./code_runner.sh


-- To see the keystrokes in the database
bin/psql postgres

-- view the keystrokes using:
SELECT * FROM keypress_log;