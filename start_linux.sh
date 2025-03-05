# creando el env
cd backend
python3 -m venv .venv

# activando el entorno
source .venv/bin/activate

# instalando dependencias
pip install -r requirements.txt
cd ..

# instalar dependencias de frotend
cd frontend
npm install
cd ..

# correr el servidor backend en segundo plano
cd backend
python3 app.py &
cd ..

# correr el servidor frontend
cd frontend
npm run dev
