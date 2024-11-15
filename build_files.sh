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

echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install all deps in the venv
pip install -r requirements.txt

# collect static files using the Python interpreter from venv
python3.9 manage.py collectstatic --noinput

echo "BUILD END"