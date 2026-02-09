#start with a base system (Oficjalny python image)
FROM python:3.11-slim

#2. Set the working directory inside the container
WORKDIR /app

#3. Copy the requirements file
COPY requirements.txt .

#4. Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

#5. copy the rest of the app's code
COPY . .

#6. Tell docker to open port 5000
EXPOSE 5100

#7. The command to run when the container starts
CMD ["python", "run.py"]

#for the deployment:
#docker build -t yourhub-app .

#for the image:
#start the docker on your computer
#docker run -p 5000:5000 yourhub-app