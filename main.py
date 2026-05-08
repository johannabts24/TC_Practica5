import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import re
from logic.strings_logic import get_prefixes, get_suffixes, get_substrings
from logic.languages_logic import get_kleene_closure, get_positive_closure
from logic.automaton_logic import Automaton 
from logic.grammar_logic import Grammar 

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador Universal de Autómatas - ESCOM")
        self.root.geometry("1400x950")
        self.root.configure(bg="#0f172a")
        
        # Inicialización de motores lógicos
        self.dfa_sim = Automaton()
        self.dfa_const = Automaton()
        self.dfa_res = None # Para guardar resultados de conversiones
        self.dfa_regex_to_af = None # Inicialización para evitar errores
        self.grammar_logic = Grammar()
        
        self.celdas_const = {}
        self.c_in = {} 

        # Colores originales
        self.temas = {
            0: {"accent": "#10b981", "btn": "#059669"}, # Verde (Cadenas)
            1: {"accent": "#fbbf24", "btn": "#d97706"}, # Amarillo (Lenguajes)
            2: {"accent": "#a855f7", "btn": "#7c3aed"}, # Morado (Simulador)
            3: {"accent": "#db2777", "btn": "#be185d"}, # Rosa (Constructor)
            4: {"accent": "#f97316", "btn": "#ea580c"}, # Naranja (Operaciones)
            5: {"accent": "#06b6d4", "btn": "#0891b2"}, # Cian (AF -> ER)
            6: {"accent": "#f87171", "btn": "#ef4444"}, # Rojo Claro (ER -> AF)
            7: {"accent": "#3b82f6", "btn": "#2563eb"}, #Azul fuerte (Aplicaciones)
            8: {"accent": "#7e22ce", "btn": "#581c87"} #Morado Fuerte (Gramaticas)
        }

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("TNotebook", background="#0f172a", borderwidth=0)
        self.style.configure("TNotebook.Tab", background="#1e293b", foreground="white", padding=[20, 8], font=("Arial", 10, "bold"))
        
        self.nb = ttk.Notebook(self.root)
        self.nb.pack(expand=True, fill="both", padx=15, pady=15)

        nombres = [" 1. CADENAS ", " 2. LENGUAJES ", " 3. SIMULADOR ", " 4. CONSTRUCTOR ", " 5. OPERACIONES ", " 6. AF ➔ ER ", " 7. ER ➔ AF ", 
                    " 8. APLICACIONES ", "9. GRAMATICAS"]
        self.tabs = [tk.Frame(self.nb, bg="#1e293b") for _ in range(9)]
        
        for tab, nom in zip(self.tabs, nombres): 
            self.nb.add(tab, text=nom)

        self.nb.bind("<<NotebookTabChanged>>", self.actualizar_estilo_pestaña)

        # Configuración de todas las pestañas
        self.setup_tab_cadenas()
        self.setup_tab_lenguajes()
        self.setup_tab_simulador()
        self.setup_tab_constructor()
        self.setup_tab_operaciones()
        self.setup_tab_af_to_er()
        self.setup_tab_er_to_af()
        self.setup_tab_aplicaciones()
        self.setup_tab_gramaticas()

    def actualizar_estilo_pestaña(self, event):
        idx = self.nb.index("current")
        color_accent = self.temas[idx]["accent"]
        self.style.map("TNotebook.Tab", background=[("selected", color_accent)], foreground=[("selected", "black")])

    # --- PESTAÑA 1: CADENAS ---
    def setup_tab_cadenas(self):
        t = self.temas[0]
        f = tk.Frame(self.tabs[0], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        tk.Label(f, text="OPERACIONES CON CADENAS", bg="#1e293b", fg=t["accent"], font=("Arial", 18, "bold")).pack(pady=10)
        self.ent_c = tk.Entry(f, font=("Consolas", 16), bg="#0f172a", fg="white", insertbackground="white", relief="flat")
        self.ent_c.pack(fill="x", pady=10)
        tk.Button(f, text="CALCULAR", command=self.run_c, bg=t["btn"], fg="white", font=("bold", 12), pady=10).pack(fill="x")
        self.txt_c = tk.Text(f, bg="#020617", fg="white", font=("Consolas", 12), pady=10, padx=10)
        self.txt_c.pack(expand=True, fill="both", pady=20)

    def run_c(self):
        s = self.ent_c.get()
        self.txt_c.delete("1.0", tk.END)
        self.txt_c.insert(tk.END, f"Prefijos: {get_prefixes(s)}\n\nSufijos: {get_suffixes(s)}\n\nSubcadenas: {get_substrings(s)}")

    # --- PESTAÑA 2: LENGUAJES ---
    def setup_tab_lenguajes(self):
        t = self.temas[1]
        f = tk.Frame(self.tabs[1], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        tk.Label(f, text="CLAUSURAS DE LENGUAJES (Σ)", bg="#1e293b", fg=t["accent"], font=("Arial", 18, "bold")).pack(pady=10)
        tk.Label(f, text="Alfabeto (sep. por comas):", bg="#1e293b", fg="white").pack(anchor="w")
        self.ent_l = tk.Entry(f, font=("Consolas", 14), bg="#0f172a", fg="white", relief="flat")
        self.ent_l.pack(fill="x", pady=5)
        tk.Label(f, text="Potencia Máxima (n):", bg="#1e293b", fg="white").pack(anchor="w")
        self.ent_n = tk.Entry(f, font=("Consolas", 14), bg="#0f172a", fg="white", relief="flat")
        self.ent_n.pack(fill="x", pady=5)
        tk.Button(f, text="CALCULAR CLAUSURAS", command=self.run_l, bg=t["btn"], fg="white", font=("bold", 12), pady=10).pack(fill="x", pady=10)
        self.txt_l = tk.Text(f, bg="#020617", fg="white", font=("Consolas", 12), pady=10, padx=10)
        self.txt_l.pack(expand=True, fill="both")

    def run_l(self):
        alpha = [x.strip() for x in self.ent_l.get().split(",") if x.strip()]
        try:
            n = int(self.ent_n.get())
            self.txt_l.delete("1.0", tk.END)
            self.txt_l.insert(tk.END, f"Σ* (Kleene):\n{get_kleene_closure(alpha, n)}\n\nΣ+ (Positiva):\n{get_positive_closure(alpha, n)}")
        except: messagebox.showerror("Error", "n debe ser entero")

    # --- PESTAÑA 3: SIMULADOR ---
    def setup_tab_simulador(self):
        t = self.temas[2]; top = tk.Frame(self.tabs[2], bg="#0f172a"); top.pack(fill="x")
        tk.Button(top, text="CARGAR ARCHIVO", command=self.importar_sim, bg=t["btn"], fg="white", font=("bold", 10), padx=15).pack(side="left", padx=20, pady=10)
        self.lbl_q = tk.Label(top, text="M = (Q, Σ, δ, q0, F)", bg="#0f172a", fg=t["accent"], font=("Consolas", 12, "bold")); self.lbl_q.pack(side="right", padx=20)
        
        paned = tk.PanedWindow(self.tabs[2], orient="horizontal", bg="#1e293b", borderwidth=0); paned.pack(fill="both", expand=True)
        self.can_sim = tk.Canvas(paned, bg="#020617", highlightthickness=1, highlightbackground=t["accent"]); paned.add(self.can_sim, stretch="always", width=800)
        self.f_tabla_sim = tk.Frame(paned, bg="#1e293b", width=400); paned.add(self.f_tabla_sim, stretch="never")
        
        bottom = tk.Frame(self.tabs[2], bg="#0f172a", pady=15); bottom.pack(fill="x")
        val_f = tk.Frame(bottom, bg="#0f172a"); val_f.pack(side="left", padx=20, anchor="n")
        self.ent_cad_sim = tk.Entry(val_f, font=("Consolas", 14), width=35, bg="#1e293b", fg="white", relief="flat"); self.ent_cad_sim.pack(pady=10)
        
        btn_f = tk.Frame(val_f, bg="#0f172a"); btn_f.pack(fill="x")
        tk.Button(btn_f, text="VALIDAR", command=self.validar_sim, bg=t["btn"], fg="white", font=("bold", 11)).pack(side="left", fill="x", expand=True, padx=2)
        tk.Button(btn_f, text="λ-CLAUSURA", command=self.ver_clausura_sim, bg="#475569", fg="white", font=("bold", 11)).pack(side="left", fill="x", expand=True, padx=2)
        tk.Button(btn_f, text="MASIVO", command=self.prueba_masiva_sim, bg="#475569", fg="white", font=("bold", 11)).pack(side="left", fill="x", expand=True, padx=2)

        self.lbl_res_sim = tk.Label(val_f, text="ESTADO: ---", bg="#0f172a", fg="white", font=("Arial", 14, "bold")); self.lbl_res_sim.pack(pady=20)
        self.txt_trace_sim = tk.Text(bottom, height=10, bg="#020617", fg=t["accent"], font=("Consolas", 11), relief="flat", padx=15, pady=10); self.txt_trace_sim.pack(side="right", padx=20, fill="both", expand=True)

    def importar_sim(self):
        p = filedialog.askopenfilename()
        if p:
            if p.endswith(".json"): self.dfa_sim.load_from_json(p)
            else: self.dfa_sim.load_from_jff(p)
            self.root.update(); self.dfa_sim.draw_on_canvas(self.can_sim)
            self.mostrar_tabla(self.f_tabla_sim, self.dfa_sim, color_accent=self.temas[2]["accent"])
            self.update_q_ui()

    def validar_sim(self):
        ok, path, final = self.dfa_sim.validate_string(self.ent_cad_sim.get())
        self.txt_trace_sim.delete("1.0", tk.END); self.txt_trace_sim.insert(tk.END, "\n".join(path))
        self.lbl_res_sim.config(text="ACEPTADA" if ok else "RECHAZADA", fg="#10b981" if ok else "#ef4444")

    def ver_clausura_sim(self):
        estado = simpledialog.askstring("λ-Clausura", "Estado:")
        if estado and estado in self.dfa_sim.states:
            clausura = self.dfa_sim.get_lambda_closure({estado})
            messagebox.showinfo("Resultado", f"E({estado}) = {clausura}")

    def prueba_masiva_sim(self):
        p = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not p: return
        with open(p, 'r') as f:
            res = [f"{c.strip()}: {'OK' if self.dfa_sim.validate_string(c.strip())[0] else 'FAIL'}" for c in f.readlines()]
        self.txt_trace_sim.delete("1.0", tk.END); self.txt_trace_sim.insert(tk.END, "--- RESULTADOS ---\n" + "\n".join(res))

    def update_q_ui(self):
        d = self.dfa_sim
        self.lbl_q.config(text=f"M = ({{{','.join(d.states)}}}, {{{','.join(d.alphabet)}}}, δ, {d.initial_state}, {{{','.join(d.final_states)}}})")

    # --- PESTAÑA 4: CONSTRUCTOR ---
    def setup_tab_constructor(self):
        t = self.temas[3]; main_f = tk.Frame(self.tabs[3], bg="#1e293b")
        main_f.pack(fill="both", expand=True, padx=10, pady=10)
        p_left = tk.Frame(main_f, bg="#1e293b", width=300); p_left.pack(side="left", fill="y", padx=(0, 10)); p_left.pack_propagate(False)
        
        for txt, key in [("Estados Q:", "q"), ("Alfabeto Σ:", "s"), ("Inicial q0:", "i"), ("Finales F:", "f")]:
            tk.Label(p_left, text=txt, bg="#1e293b", fg=t["accent"], font=("bold", 9)).pack(anchor="w")
            e = tk.Entry(p_left, bg="#0f172a", fg="white", insertbackground="white", relief="flat"); e.pack(fill="x", pady=2); self.c_in[key] = e
        
        tk.Button(p_left, text="GENERAR MATRIZ", command=self.gen_matriz_c, bg=t["btn"], fg="white", font=("bold", 9), pady=8).pack(fill="x", pady=10)
        tk.Button(p_left, text="GUARDAR JFF", command=self.exportar_jff_c, bg="#475569", fg="white", font=("bold", 8)).pack(fill="x", pady=2)
        self.f_m_c = tk.Frame(p_left, bg="#0f172a"); self.f_m_c.pack(fill="both", expand=True, pady=10)

        p_right = tk.Frame(main_f, bg="#1e293b"); p_right.pack(side="right", fill="both", expand=True)
        # CORRECCIÓN AQUÍ: Se eliminó 'weight=1' que causaba el TclError
        self.can_c = tk.Canvas(p_right, bg="#020617", height=450, highlightthickness=1, highlightbackground=t["accent"])
        self.can_c.pack(fill="both", expand=True, padx=5)
        
        bottom_c = tk.Frame(p_right, bg="#1e293b", pady=15); bottom_c.pack(fill="both", expand=True)
        val_f_c = tk.Frame(bottom_c, bg="#1e293b"); val_f_c.pack(side="left", padx=10, anchor="n")
        self.ent_val_c = tk.Entry(val_f_c, font=("Consolas", 14), width=25, bg="#0f172a", fg="white", relief="flat"); self.ent_val_c.pack(pady=10)
        tk.Button(val_f_c, text="DIBUJAR Y VALIDAR", command=self.upd_and_test_c, bg=t["btn"], fg="white", font=("bold", 10), pady=5).pack(fill="x")
        self.lbl_res_c = tk.Label(val_f_c, text="ESTADO: ---", bg="#1e293b", fg="white", font=("Arial", 14, "bold")); self.lbl_res_c.pack(pady=20)
        self.txt_trace_c = tk.Text(bottom_c, height=8, bg="#020617", fg=t["accent"], font=("Consolas", 11), relief="flat", padx=10, pady=10); self.txt_trace_c.pack(side="right", padx=10, fill="both", expand=True)

    def gen_matriz_c(self):
        self.dfa_const.states = [x.strip() for x in self.c_in['q'].get().split(",") if x.strip()]
        self.dfa_const.alphabet = [x.strip() for x in self.c_in['s'].get().split(",") if x.strip()]
        self.celdas_const = self.mostrar_tabla(self.f_m_c, self.dfa_const, editable=True, color_accent=self.temas[3]["accent"])

    def sync_dfa_const(self):
        self.dfa_const.states = [x.strip() for x in self.c_in['q'].get().split(",") if x.strip()]
        self.dfa_const.alphabet = [x.strip() for x in self.c_in['s'].get().split(",") if x.strip()]
        self.dfa_const.initial_state = self.c_in['i'].get().strip()
        self.dfa_const.final_states = [x.strip() for x in self.c_in['f'].get().split(",") if x.strip()]
        self.dfa_const.transitions = {}
        for (q, a), ent in self.celdas_const.items():
            dest_str = ent.get().strip()
            if dest_str: 
                for d in dest_str.split(","): self.dfa_const.add_transition(q, a, d.strip())

    def upd_and_test_c(self):
        self.sync_dfa_const(); self.root.update(); self.dfa_const.draw_on_canvas(self.can_c)
        ok, path, _ = self.dfa_const.validate_string(self.ent_val_c.get())
        self.txt_trace_c.delete("1.0", tk.END); self.txt_trace_c.insert(tk.END, "\n".join(path))
        self.lbl_res_c.config(text="ACEPTADA" if ok else "RECHAZADA", fg="#10b981" if ok else "#ef4444")

    def exportar_jff_c(self):
        self.sync_dfa_const(); p = filedialog.asksaveasfilename(defaultextension=".jff")
        if p: self.dfa_const.save_to_jff(p); messagebox.showinfo("Éxito", "Guardado JFF.")

    # --- PESTAÑA 5: OPERACIONES ---
    def setup_tab_operaciones(self):
        t = self.temas[4]; main_f = tk.Frame(self.tabs[4], bg="#1e293b")
        main_f.pack(fill="both", expand=True, padx=10, pady=10)
        
        top = tk.Frame(main_f, bg="#0f172a"); top.pack(fill="x", pady=5)
        tk.Button(top, text="CARGAR ORIGINAL", command=self.cargar_op, bg="#475569", fg="white", font=("bold", 9)).pack(side="left", padx=10, pady=10)
        tk.Button(top, text="CONVERTIR AFN ➔ AFD", command=self.convertir_afd, bg=t["btn"], fg="white", font=("bold", 10), padx=15).pack(side="left", padx=5)
        tk.Button(top, text="MINIMIZAR AFD", command=self.minimizar_afd, bg=t["btn"], fg="white", font=("bold", 10), padx=15).pack(side="left", padx=5)
        tk.Button(top, text="GUARDAR RESULTADO", command=self.guardar_op, bg="#fbbf24", fg="black", font=("bold", 10), padx=15).pack(side="right", padx=10)

        paned = tk.PanedWindow(main_f, orient="horizontal", bg="#1e293b", borderwidth=0); paned.pack(fill="both", expand=True)
        
        f_izq = tk.Frame(paned, bg="#020617"); paned.add(f_izq, stretch="always")
        tk.Label(f_izq, text="ORIGINAL", bg="#020617", fg=t["accent"], font=("bold", 10)).pack()
        self.can_op_izq = tk.Canvas(f_izq, bg="#020617", highlightthickness=1, highlightbackground=t["accent"])
        self.can_op_izq.pack(fill="both", expand=True, padx=2, pady=2)
        
        f_der = tk.Frame(paned, bg="#020617"); paned.add(f_der, stretch="always")
        self.lbl_op_res = tk.Label(f_der, text="RESULTADO", bg="#020617", fg=t["accent"], font=("bold", 10))
        self.lbl_op_res.pack()
        self.can_op_der = tk.Canvas(f_der, bg="#020617", highlightthickness=1, highlightbackground=t["accent"])
        self.can_op_der.pack(fill="both", expand=True, padx=2, pady=2)
        
        self.txt_op = tk.Text(main_f, height=6, bg="#0f172a", fg="white", font=("Consolas", 10), relief="flat"); self.txt_op.pack(fill="x", pady=10)

    def cargar_op(self):
        p = filedialog.askopenfilename()
        if p:
            self.dfa_op = Automaton()
            if p.endswith(".json"): self.dfa_op.load_from_json(p)
            else: self.dfa_op.load_from_jff(p)
            self.root.update(); self.dfa_op.draw_on_canvas(self.can_op_izq)

    def convertir_afd(self):
        if not hasattr(self, 'dfa_op'): return
        self.dfa_res = self.dfa_op.to_dfa()
        self.root.update(); self.dfa_res.draw_on_canvas(self.can_op_der)
        self.txt_op.insert(tk.END, f"\n[INFO] AFN convertido a AFD exitosamente.")

    def minimizar_afd(self):
        if not hasattr(self, 'dfa_op'): return
        min_dfa, o, m, p = self.dfa_op.minimize()
        self.dfa_res = min_dfa
        self.root.update(); self.dfa_res.draw_on_canvas(self.can_op_der)
        self.txt_op.insert(tk.END, f"\n[MIN] Original: {o} est. -> Mínimo: {m} est. (Clases: {p})")

    def guardar_op(self):
        if not self.dfa_res: return
        p = filedialog.asksaveasfilename(defaultextension=".jff")
        if p: self.dfa_res.save_to_jff(p)

    # --- PESTAÑA 6: AF -> ER ---
    def setup_tab_af_to_er(self):
        t = self.temas[5]
        f = tk.Frame(self.tabs[5], bg="#1e293b", padx=40, pady=40)
        f.pack(expand=True, fill="both")
        tk.Label(f, text="AF ➔ EXPRESIÓN REGULAR", bg="#1e293b", fg=t["accent"], font=("Arial", 22, "bold")).pack(pady=10)
        
        btn_gen = tk.Button(f, text="GENERAR EXPRESIÓN REGULAR", command=self.generar_er, 
                           bg=t["btn"], fg="white", font=("bold", 13), padx=40, pady=12)
        btn_gen.pack(pady=20)

        res_container = tk.Frame(f, bg="#0f172a", padx=15, pady=15, highlightthickness=2, highlightbackground=t["accent"])
        res_container.pack(fill="both", expand=True, pady=10)
        
        self.txt_er_res = tk.Text(res_container, font=("Consolas", 18, "bold"), bg="#020617", 
                                  fg="#5eead4", relief="flat", wrap="none", height=8)
        self.txt_er_res.pack(side="top", fill="both", expand=True)
        
        h_scroll = tk.Scrollbar(res_container, orient="horizontal", command=self.txt_er_res.xview)
        h_scroll.pack(side="bottom", fill="x")
        self.txt_er_res.config(xscrollcommand=h_scroll.set)

    def generar_er(self):
        target = self.dfa_res if self.dfa_res else (self.dfa_op if hasattr(self, 'dfa_op') else None)
        if target:
            try:
                self.txt_er_res.delete("1.0", tk.END)
                # Requiere implementar 'to_regex' en logic/automaton_logic.py
                self.txt_er_res.insert("1.0", target.to_regex())
            except AttributeError:
                messagebox.showerror("Error", "El método 'to_regex' no está implementado en logic/automaton_logic.py")
        else:
            messagebox.showwarning("Aviso", "Carga o procesa un autómata en la pestaña de Operaciones primero.")

    # --- PESTAÑA 7: ER -> AF ---
    def setup_tab_er_to_af(self):
        t = self.temas[6]
        f = tk.Frame(self.tabs[6], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        tk.Label(f, text="EXPRESIÓN REGULAR ➔ AUTÓMATA", bg="#1e293b", fg=t["accent"], font=("Arial", 22, "bold")).pack(pady=10)
        
        entry_f = tk.Frame(f, bg="#1e293b")
        entry_f.pack(fill="x", pady=20)
        tk.Label(entry_f, text="Ingresa la ER:", bg="#1e293b", fg="white").pack(anchor="w")
        self.ent_er_input = tk.Entry(entry_f, font=("Consolas", 18), bg="#0f172a", fg="white", relief="flat")
        self.ent_er_input.pack(fill="x", pady=10)

        btn_f = tk.Frame(f, bg="#1e293b")
        btn_f.pack(pady=10)
        tk.Button(btn_f, text="CONSTRUIR", command=self.er_a_afn, bg=t["btn"], fg="white", font=("bold", 12), padx=25).pack(side="left", padx=10)
        tk.Button(btn_f, text="GUARDAR .JFF", command=self.guardar_er_af, bg="#475569", fg="white", font=("bold", 12), padx=25).pack(side="left", padx=10)

        self.can_er_af = tk.Canvas(f, bg="#020617", highlightthickness=2, highlightbackground=t["accent"])
        self.can_er_af.pack(fill="both", expand=True, pady=20)

    def er_a_afn(self):
        regex = self.ent_er_input.get().strip()
        if regex:
            try:
                # 1. Construcción inicial (Genera el autómata con muchos estados y lambdas)
                base_automaton = Automaton()
                # Compatibilidad de símbolos: tratamos ε como λ
                base_automaton.from_regex(regex.replace("ε", "λ"))
                
                # 2. Transformación a AFD (Elimina las transiciones λ)
                dfa_version = base_automaton.to_dfa()
                
                # 3. Minimización (Reduce el número de estados al mínimo posible)
                # Usamos el método minimize() que devuelve (min_dfa, o, m, p)
                self.dfa_regex_to_af, _, _, _ = dfa_version.minimize()
                
                # 4. Dibujar el resultado final simplificado
                self.root.update()
                self.dfa_regex_to_af.draw_on_canvas(self.can_er_af)
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo simplificar el autómata: {str(e)}")

    def guardar_er_af(self):
        if hasattr(self, 'dfa_regex_to_af') and self.dfa_regex_to_af:
            p = filedialog.asksaveasfilename(defaultextension=".jff")
            if p: self.dfa_regex_to_af.save_to_jff(p)

    # --- PESTAÑA 8: APLICACIONES ---
    def setup_tab_aplicaciones(self):
        t = self.temas[7]
        f = tk.Frame(self.tabs[7], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        
        tk.Label(f, text="APLICACIONES DE EXPRESIONES REGULARES", bg="#1e293b", fg=t["accent"], font=("Arial", 20, "bold")).pack(pady=10)
        
        # Panel de Controles
        ctrl_f = tk.Frame(f, bg="#1e293b")
        ctrl_f.pack(fill="x", pady=10)
        
        tk.Label(ctrl_f, text="Tipo de Dato:", bg="#1e293b", fg="white", font=("Arial", 12)).pack(side="left")
        self.combo_app = ttk.Combobox(ctrl_f, values=["Correo Electrónico", "URL", "Fecha (DD/MM/AAAA)"], state="readonly", font=("Arial", 12), width=20)
        self.combo_app.current(0)
        self.combo_app.pack(side="left", padx=10)
        
        tk.Label(ctrl_f, text="Texto:", bg="#1e293b", fg="white", font=("Arial", 12)).pack(side="left", padx=(15, 0))
        self.ent_app_input = tk.Entry(ctrl_f, font=("Consolas", 14), bg="#0f172a", fg="white", relief="flat")
        self.ent_app_input.pack(side="left", fill="x", expand=True, padx=10)
        
        tk.Button(ctrl_f, text="VALIDAR Y GRAFICAR", command=self.ejecutar_aplicacion, bg=t["btn"], fg="white", font=("bold", 11), padx=15).pack(side="left")

        # Panel de Retroalimentación
        feed_f = tk.Frame(f, bg="#0f172a", pady=10, highlightthickness=1, highlightbackground=t["accent"])
        feed_f.pack(fill="x", pady=15)
        self.lbl_app_res = tk.Label(feed_f, text="Esperando entrada...", bg="#0f172a", font=("Arial", 14, "bold"), fg="white")
        self.lbl_app_res.pack()
        self.lbl_app_sug = tk.Label(feed_f, text="", bg="#0f172a", font=("Arial", 11), fg="#fbbf24")
        self.lbl_app_sug.pack(pady=5)

    # --- PESTAÑA 9: GRAMÁTICAS ---
    def setup_tab_gramaticas(self):
        t = self.temas[8]
        f = tk.Frame(self.tabs[8], bg="#1e293b", padx=30, pady=30)
        f.pack(expand=True, fill="both")
        
        tk.Label(f, text="TRANSFORMACIÓN DE GRAMÁTICAS A FNC", bg="#1e293b", 
                 fg=t["accent"], font=("Arial", 22, "bold")).pack(pady=10)
        
        # Panel de Entrada
        in_f = tk.Frame(f, bg="#1e293b")
        in_f.pack(fill="x", pady=10)
        tk.Label(in_f, text="Ingresa producciones (Ej: S -> aA | b):", bg="#1e293b", 
                 fg="white", font=("Arial", 11)).pack(anchor="w")
        
        self.txt_gram_in = tk.Text(in_f, height=5, font=("Consolas", 14), bg="#0f172a", 
                                   fg="white", insertbackground="white", relief="flat")
        self.txt_gram_in.pack(fill="x", pady=10)
        
        # Panel de Botones
        btn_f = tk.Frame(f, bg="#1e293b")
        btn_f.pack(fill="x", pady=5)
        
        tk.Button(btn_f, text="TRANSFORMAR A FNC", command=self.ejecutar_fnc, 
                  bg=t["btn"], fg="white", font=("bold", 11), padx=20, pady=10).pack(side="left", padx=5)
        
        tk.Button(btn_f, text="EXPORTAR JFF", command=self.guardar_jff_gramatica, 
                  bg="#10b981", fg="white", font=("bold", 11), padx=20, pady=10).pack(side="right", padx=5)

        # Panel de Resultados (Paso a Paso)
        tk.Label(f, text="BITÁCORA DE TRANSFORMACIÓN:", bg="#1e293b", 
                 fg=t["accent"], font=("Arial", 12, "bold")).pack(anchor="w", pady=(20, 5))
        
        self.txt_gram_res = tk.Text(f, font=("Consolas", 13), bg="#000000", 
                                    fg="#22d3ee", relief="flat", padx=15, pady=15)
        self.txt_gram_res.pack(fill="both", expand=True)

    def ejecutar_fnc(self):
        raw_text = self.txt_gram_in.get("1.0", tk.END).strip()
        if not raw_text:
            messagebox.showwarning("Aviso", "Por favor, ingresa una gramática.")
            return
        
        self.grammar_logic.load_from_text(raw_text)
        pasos = self.grammar_logic.to_chomsky()
        
        self.txt_gram_res.delete("1.0", tk.END)
        self.txt_gram_res.insert("1.0", pasos)

    def guardar_jff_gramatica(self):
        if not self.grammar_logic.productions:
            messagebox.showerror("Error", "No hay una gramática procesada para guardar.")
            return
            
        p = filedialog.asksaveasfilename(defaultextension=".jff", 
                                         filetypes=[("JFLAP Grammar", "*.jff")])
        if p:
            self.grammar_logic.save_to_jff(p)
            messagebox.showinfo("Éxito", f"Archivo guardado en:\n{p}")

        # Canvas para el Autómata
        tk.Label(f, text="Autómata Finito Estructural (Versión Didáctica)", bg="#1e293b", fg=t["accent"], font=("Arial", 10, "italic")).pack(anchor="w")
        self.can_app = tk.Canvas(f, bg="#020617", highlightthickness=1, highlightbackground=t["accent"])
        self.can_app.pack(fill="both", expand=True)

    def ejecutar_aplicacion(self):
        tipo = self.combo_app.get()
        texto = self.ent_app_input.get().strip()
        
        # 1. Definir ER estricta (re) y ER didáctica estructural (Thompson Canvas)
        if tipo == "Correo Electrónico":
            patron_estricto = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            # CAMBIO: Usamos 'p' para representar el punto literal y evitar conflictos
            er_didactica = "(u|p)*@(d)*p(c|o|m)" 
            sugerencia_gen = "Formato esperado: usuario@dominio.com."
        elif tipo == "URL":
            patron_estricto = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'
            # CAMBIO: Simplificamos para que el algoritmo de Thompson no se confunda
            er_didactica = "(h|t|p|s)*:(/|/)*(w)*p(d)*p(c|o)"
            sugerencia_gen = "Formato esperado: http://www.sitio.com o www.sitio.com."
        else: # Fecha
            patron_estricto = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/\d{4}$'
            er_didactica = "(d|d)/(m|m)/(a|a|a|a)"
            sugerencia_gen = "Formato esperado: DD/MM/AAAA. Revisa que el mes sea <= 12."

        # 2. Validación de Retroalimentación Inteligente
        if re.match(patron_estricto, texto):
            self.lbl_app_res.config(text="✓ VALIDACIÓN EXITOSA", fg="#10b981")
            self.lbl_app_sug.config(text="El texto cumple correctamente con las reglas de la expresión regular.")
        else:
            self.lbl_app_res.config(text="✕ TEXTO INVÁLIDO", fg="#ef4444")
            
            # Análisis específico de errores
            sugerencia = sugerencia_gen
            if tipo == "Correo Electrónico":
                if "@" not in texto: sugerencia = "Error: Falta el símbolo '@' en tu correo."
                elif "." not in texto.split("@")[-1]: sugerencia = "Error: Falta el punto '.' en el dominio (ej. .com, .mx)."
            elif tipo == "URL":
                if " " in texto: sugerencia = "Error: Una URL no puede contener espacios en blanco."
            elif tipo == "Fecha (DD/MM/AAAA)":
                if "-" in texto: sugerencia = "Error: Utiliza barras diagonales '/' en lugar de guiones '-'."
                elif len(texto.split("/")) != 3: sugerencia = "Error: Faltan separadores de Día, Mes o Año."
            
            self.lbl_app_sug.config(text=f"Sugerencia: {sugerencia}")

        # 3. Dibujar el Autómata Didáctico
        try:
            if not hasattr(self, 'dfa_app'):
                self.dfa_app = Automaton() # Reutilizamos la c del simulador
            
            self.dfa_app.from_regex(er_didactica)
            self.root.update()
            self.dfa_app.draw_on_canvas(self.can_app)
        except Exception as e:
            messagebox.showerror("Error de Graficación", f"Error al generar AFN: {str(e)}")

    # --- UTILIDAD: DIBUJO DE TABLAS ---
    def mostrar_tabla(self, frame, dfa_obj, editable=False, color_accent="#38bdf8"):
        for w in frame.winfo_children(): w.destroy()
        h_bg = "#334155"; c_w = 10
        tk.Label(frame, text="δ", bg=h_bg, fg=color_accent, width=c_w, font=("bold", 10)).grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        for j, a in enumerate(dfa_obj.alphabet):
            tk.Label(frame, text=a, bg=h_bg, fg=color_accent, width=c_w, font=("bold", 10)).grid(row=0, column=j+1, sticky="nsew", padx=1, pady=1)
        
        dict_r = {}
        for i, q in enumerate(dfa_obj.states):
            tk.Label(frame, text=q, bg=h_bg, fg="white", width=c_w, font=("bold", 10)).grid(row=i+1, column=0, sticky="nsew", padx=1, pady=1)
            for j, a in enumerate(dfa_obj.alphabet):
                dest_set = dfa_obj.transitions.get((q, a), set())
                v = ",".join(dest_set)
                if editable:
                    e = tk.Entry(frame, width=c_w, justify="center", bg="#1e293b", fg="white", relief="flat", insertbackground="white")
                    e.insert(0, v); e.grid(row=i+1, column=j+1, sticky="nsew", padx=1, pady=1); dict_r[(q, a)] = e
                else:
                    tk.Label(frame, text=v if v else "-", bg="#0f172a", fg="white", width=c_w).grid(row=i+1, column=j+1, sticky="nsew", padx=1, pady=1)
        return dict_r

if __name__ == "__main__":
    root = tk.Tk(); app = App(root); root.mainloop()