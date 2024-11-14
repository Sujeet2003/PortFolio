# Step 1: Install dependencies
# echo "Installing dependencies..."
# pip3 install --upgrade pip
# pip3 install -r requirements.txt

# # Step 2: Collect static files
# echo "Collecting static files..."
# python3 manage.py collectstatic --noinput

# # Step 3: Apply database migrations
# echo "Running database migrations..."
# python3 manage.py migrate --noinput

# # Step 4: Confirm completion
# echo "Build process completed successfully!"


python3.11 -m pip uninstall psycopg2-binary -y
python3.11 -m pip install psycopg2-binary==2.9.9 --no-cache-dir
#!/bin/bash

echo "Updating system packages..."
apt-get update
apt-get install -y libpq-dev python3-dev

echo "Updating pip..."
python3.11 -m pip install -U pip

# Install dependencies
echo "Installing project dependencies..."
python3.11 -m pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3.11 manage.py collectstatic --noinput --clear

echo "Build process completed!"
