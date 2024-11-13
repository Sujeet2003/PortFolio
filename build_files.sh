# Step 1: Install dependencies
echo "Installing dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Step 2: Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Step 3: Apply database migrations
echo "Running database migrations..."
python3 manage.py migrate --noinput

# Step 4: Confirm completion
echo "Build process completed successfully!"
