FROM python:3.9

WORKDIR /tmp

# Copy the dependencies and the script
COPY src/requirements.txt .
COPY src/convert.py .

# Upgrade pip
RUN pip install --upgrade pip
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the script
CMD ["python", "convert.py"]
