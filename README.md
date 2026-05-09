# 🎉 EUREKA! — College Lost & Found Platform

> *"The classic cry of discovery"*

A beautiful, production-ready web application for managing lost and found items on a college campus. Built with modern web technologies and powered by Supabase.

---

## ✨ **Key Features**

- 🎨 **Modern Dark UI** — sleek charcoal/navy design with purple-blue accents and smooth glassmorphism effects
- 📌 **Sticky Navigation** — easy access to all sections with smooth scrolling
- 🎯 **Hero Section** — eye-catching animated gradient title with live statistics and visual effects
- 📋 **Smart Listings** — preview 4 items on homepage with full catalog access
- 🔄 **Lost / Found Toggle** — instantly switch between lost and found items
- 🔍 **Real-Time Search** — filter by keyword, category, location, and date
- 💬 **Item Details Modal** — click any card to view complete information
- 👤 **User Authentication** — login and signup with secure password management
- ➕ **Report Items** — submit new lost or found items easily
- 🔔 **Notifications** — get instant feedback on your actions
- ⚡ **Fully Responsive** — works great on desktop, tablet, and mobile

---

## 🚀 **Quick Start Guide**

### **Step 1: Install Dependencies**

Make sure you have Node.js installed, then run:

```bash
npm install
```

### **Step 2: Set Up Supabase (Optional)**

Supabase is optional — the app works with built-in mock data for testing!

If you want to use a real database:

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Copy the file `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Fill in your Supabase details:
   ```env
   VITE_SUPABASE_URL=https://your-project.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-key-here
   ```

### **Step 3: Run Locally**

```bash
npm run dev
```

Then open **http://localhost:5173** in your web browser. 🎉

---

## 🗄️ **Supabase Database Setup**

If you want to use Supabase with real data:

1. Open your Supabase project dashboard
2. Go to **SQL Editor** → **New Query**
3. Copy and paste the contents of `supabase-schema.sql`
4. Click **Run** to create the database tables and sample data
5. Go to **Settings** → **API** and copy:
   - **Project URL** → paste into `.env` as `VITE_SUPABASE_URL`
   - **anon public key** → paste into `.env` as `VITE_SUPABASE_ANON_KEY`

> **💡 Tip:** Don't have Supabase set up? No problem! The app automatically uses mock data so you can develop and demo without a backend.

---

## 📁 **Project Structure**

```
EUREKA-/
├── index.html                 # Main HTML file with SEO tags
├── src/
│   ├── main.js               # All app logic (UI, forms, modals)
│   ├── style.css             # Complete design system & animations
│   └── supabase.js           # Supabase setup + mock data fallback
├── supabase-schema.sql       # Database schema (run in Supabase)
├── vercel.json               # Vercel deployment config
├── netlify.toml              # Netlify deployment config
├── .env.example              # Template for environment variables
├── .env                      # Your private keys (never commit this)
└── README.md                 # You are here!
```

---

## ☁️ **Deployment**

### **Deploy to Vercel**

**Option 1: Using Vercel CLI**
```bash
npm install -g vercel
vercel
```

**Option 2: Using GitHub**
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com) and import your repository
3. Add environment variables:
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
4. Deploy!

### **Deploy to Netlify**

**Option 1: Using Netlify CLI**
```bash
npm install -g netlify-cli
netlify deploy --prod --dir dist
```

**Option 2: Manual Upload**
1. Build the project: `npm run build`
2. Go to [netlify.com](https://app.netlify.com)
3. Drag and drop the `dist/` folder
4. Add environment variables in **Site Settings** → **Environment Variables**

> **Remember:** Add your Supabase keys to your deployment platform's environment variables!

---

## 🛠️ **Technology Stack**

| Component | Technology |
|-----------|-----------|
| **Build Tool** | Vite 8 |
| **Frontend** | Vanilla JavaScript (ES Modules) |
| **Styling** | Pure CSS with custom design system |
| **Database** | Supabase (PostgreSQL) |
| **Authentication** | Supabase Auth |
| **Fonts** | Inter + Space Grotesk (Google Fonts) |
| **Hosting** | Vercel or Netlify |

---

## 📚 **How It Works**

### **Home Page**
- See a preview of 4 recent items
- Check live stats (items count, users)
- Browse or search items

### **Browse All Items**
- Click "View All" to see the complete catalog
- Filter by Lost/Found, category, location, or date
- Click any item card for full details

### **Report an Item**
- Click "Report Item" button
- Fill in the form (title, category, location, etc.)
- Submit and get instant confirmation

### **User Account**
- Sign up with email and password
- Log in to track your reported items
- Secure password management

---

## 🔐 **Security Notes**

- All database access uses Supabase Row Level Security (RLS)
- Your environment variables are never exposed to users
- Passwords are securely hashed in Supabase
- The mock data is only used when Supabase is not configured

---

## 🐛 **Troubleshooting**

**"I see mock data instead of real data"**
- Check that `.env` file exists and has correct Supabase keys
- Verify your Supabase project is active and `items` table exists
- Check browser console for error messages

**"npm install fails"**
- Delete `node_modules/` and `package-lock.json`
- Run `npm install` again
- Make sure you have Node.js 16+ installed

**"Port 5173 already in use"**
- Run `npm run dev -- --port 3000` to use a different port

---

## 📝 **License**

MIT License — feel free to use and modify for your campus project!

---

## 💡 **Need Help?**

- Check the [Vite documentation](https://vitejs.dev)
- Learn more at [Supabase docs](https://supabase.com/docs)
- Need support? Open an issue in this repository!

**Happy discovering! 🎉**
