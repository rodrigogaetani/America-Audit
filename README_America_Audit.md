# America Audit

**America Audit — Automatización Tributaria** es una plataforma orientada a firmas contables y de auditoría en Guatemala para automatizar procesos tributarios, contables y documentales relacionados con SAT, FEL, RTU, compras, ventas, clasificación de gastos, crédito fiscal, declaraciones y revisión tributaria.

> **Estado actual:** desarrollo activo — preparación de **America Audit Desktop 1.0.0** para Windows.

---

## Objetivo

El proyecto busca convertir tareas repetitivas de una firma contable en un flujo trazable, automatizado y revisable por humanos.

Entre sus objetivos principales están:

- importar archivos descargados desde la Agencia Virtual de SAT;
- convertir formatos SAT al formato requerido por el sistema contable;
- procesar compras y ventas;
- identificar bienes y servicios;
- clasificar gastos;
- evaluar deducibilidad para ISR;
- evaluar procedencia de crédito fiscal IVA;
- procesar documentos FEL y RTU;
- generar libros, conciliaciones y reportes;
- preparar borradores de declaraciones tributarias;
- mantener trazabilidad y bitácora de auditoría;
- permitir revisión humana de excepciones.

La filosofía del sistema es:

> **La IA interpreta; las reglas tributarias determinan; el usuario valida los casos excepcionales.**

---

## America Audit Desktop 1.0

La versión de escritorio está diseñada para ejecutarse como una aplicación normal de Windows.

El objetivo de distribución es:

```text
AmericaAudit_Setup_1.0.0.exe
```

El usuario final no debería necesitar instalar ni conocer:

- Python
- Node.js
- npm
- FastAPI
- PostgreSQL
- Docker
- Git

La aplicación se instalará mediante un setup de Windows y utilizará una interfaz gráfica de escritorio.

---

## Arquitectura

La arquitectura Desktop prevista es:

```text
AmericaAudit.exe
        │
        ▼
Desktop Launcher
        │
        ├── configuración
        ├── inicialización
        ├── migraciones
        ├── logging
        └── control de ciclo de vida
        │
        ▼
FastAPI local
        │
        ▼
React Production Build
        │
        ▼
pywebview
        │
        ▼
Ventana Desktop de Windows
```

Persistencia local:

```text
SQLite
```

Datos de usuario:

```text
%LOCALAPPDATA%\AmericaAudit\
```

Estructura esperada:

```text
AmericaAudit/
├── database/
│   └── america_audit.db
├── documents/
├── imports/
├── exports/
├── backups/
├── logs/
└── config/
```

Los datos tributarios y documentos del usuario no deben almacenarse dentro de `Program Files`.

---

## Stack tecnológico

### Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- SQLite para Desktop
- PostgreSQL como opción futura para despliegues Server

### Frontend

- React
- TypeScript
- Build de producción integrado en la aplicación

### Desktop

- pywebview
- PyInstaller
- Inno Setup

### Automatización e IA

La aplicación puede operar en modo determinístico sin IA.

La integración con modelos de lenguaje es opcional y se reserva principalmente para tareas como:

- clasificación semántica;
- interpretación de conceptos ambiguos;
- extracción documental;
- explicación de hallazgos;
- apoyo a revisión.

Los cálculos tributarios deben permanecer determinísticos, versionados y trazables.

---

## Funcionalidades principales

### Clientes y períodos

- administración de clientes;
- períodos fiscales;
- estados de revisión;
- trazabilidad de cambios.

### Importación SAT

- compras;
- ventas;
- archivos `.xls`;
- archivos `.xlsx`;
- normalización de formatos;
- validación de totales;
- exportación al formato del sistema contable.

### FEL y documentos

- PDF;
- XML cuando corresponda;
- detección de duplicados;
- hash de documentos;
- extracción estructurada;
- revisión de excepciones.

### Perfil tributario

- información RTU;
- régimen;
- obligaciones;
- parámetros tributarios aplicables.

### Clasificación de gastos

- bien / servicio;
- categoría contable;
- deducible / no deducible;
- crédito fiscal IVA;
- revisión manual cuando exista incertidumbre.

### Revisión tributaria

- reglas versionadas;
- hallazgos;
- excepciones;
- conciliaciones;
- bitácora de auditoría.

### Declaraciones

Preparación de borradores para revisión de formularios como:

- SAT-1311
- SAT-1331
- SAT-1361
- SAT-1608
- SAT-2046
- SAT-2237

Las declaraciones generadas por el sistema deben considerarse **borradores para revisión humana**.

---

## Integridad de datos

El sistema debe comprobar consistencia entre etapas.

Ejemplo:

```text
SUMA IMPORTADA
vs
SUMA NORMALIZADA
vs
SUMA CLASIFICADA
vs
SUMA EXPORTADA
```

Si existe una diferencia, el sistema no debe continuar silenciosamente.

Ejemplo de hallazgo:

```text
AA-REC-001 — Diferencia entre compras importadas y libro generado.
```

---

## Seguridad

Principios básicos:

- contraseñas almacenadas mediante hash;
- API keys fuera del código fuente;
- sanitización de nombres de archivo;
- protección contra path traversal;
- validación de extensiones;
- manejo seguro de uploads;
- hashes para detección de duplicados;
- logs sin secretos;
- datos persistentes fuera de la carpeta de instalación;
- RBAC y permisos de usuario.

---

## Desarrollo

### Backend

Ejemplo de entorno local:

```bash
cd backend
python -m venv .venv
```

En Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Ejecutar:

```powershell
uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Build de producción:

```bash
npm run build
```

---

## Build de Windows

La distribución Desktop se construye mediante:

```text
build_windows.ps1
```

Objetivo:

```powershell
.\build_windows.ps1
```

Pipeline previsto:

```text
Tests backend
    ↓
Checks frontend
    ↓
React production build
    ↓
PyInstaller
    ↓
AmericaAudit.exe
    ↓
Inno Setup
    ↓
AmericaAudit_Setup_1.0.0.exe
```

Artefactos esperados:

```text
release/
├── AmericaAudit_Setup_1.0.0.exe
└── AmericaAudit_Setup_1.0.0.exe.sha256
```

---

## GitHub Actions

El repositorio está preparado para evolucionar hacia un pipeline de CI/CD con runner Windows.

El objetivo es que cada release pueda generar automáticamente:

```text
AmericaAudit_Setup_<version>.exe
```

mediante `windows-latest`, PyInstaller e Inno Setup.

---

## Definition of Done — Desktop 1.0

America Audit Desktop 1.0 se considera listo cuando:

- puede construirse `AmericaAudit.exe`;
- puede construirse `AmericaAudit_Setup_1.0.0.exe`;
- puede instalarse en Windows 10/11 x64;
- no requiere Python en la PC del usuario;
- no requiere Node.js;
- no requiere PostgreSQL;
- no requiere Docker;
- inicia desde un acceso directo;
- el backend inicia automáticamente;
- SQLite funciona;
- puede crear clientes y períodos;
- puede importar documentos;
- puede ejecutar los módulos tributarios disponibles;
- puede exportar archivos;
- conserva los datos entre ejecuciones;
- se cierra sin dejar procesos zombie;
- los tests relevantes pasan.

---

## Estado del proyecto

Actualmente el proyecto se encuentra en fase de **productización Desktop y empaquetado para Windows**.

Prioridades:

1. integridad de datos tributarios;
2. estabilidad;
3. build reproducible de Windows;
4. persistencia local;
5. backups;
6. trazabilidad;
7. UX de escritorio;
8. CI/CD.

---

## Aviso

America Audit es una herramienta de apoyo contable y tributario.

Los resultados, clasificaciones, cálculos y borradores de declaraciones deben ser revisados por personal responsable antes de su presentación o uso oficial.

El sistema no debe presentar declaraciones automáticamente ante SAT sin un flujo explícito de validación y autorización.

---

## Licencia

Repositorio privado / uso interno de America Audit, salvo que se defina una licencia distinta en el futuro.

---

## Versión

**America Audit Desktop 1.0.0**

Desarrollo en curso.
