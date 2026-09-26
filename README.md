# America Audit

**America Audit — Automatización Tributaria** es una plataforma orientada a firmas contables y de auditoría en Guatemala para automatizar procesos tributarios, contables y documentales relacionados con SAT, FEL, RTU, compras, ventas, clasificación de gastos, crédito fiscal, declaraciones y revisión tributaria.

> **Estado actual:** desarrollo activo — preparación de **America Audit Desktop 1.0.0** para Windows.

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

> **La IA interpreta; las reglas tributarias determinan; el usuario valida los casos excepcionales.**

## America Audit Desktop 1.0

El objetivo de distribución es:

```text
AmericaAudit_Setup_1.0.0.exe
```

El usuario final no debería necesitar instalar Python, Node.js, PostgreSQL, Docker ni Git.

## Arquitectura

```text
AmericaAudit.exe
        │
        ▼
Desktop Launcher
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

Persistencia local: **SQLite**

Datos de usuario:

```text
%LOCALAPPDATA%\AmericaAudit\
```

## Stack tecnológico

- Python / FastAPI
- SQLAlchemy / Alembic
- React / TypeScript
- SQLite para Desktop
- PostgreSQL como opción futura Server
- pywebview
- PyInstaller
- Inno Setup

## Funcionalidades principales

- Clientes y períodos fiscales
- Importación de compras y ventas SAT
- Conversión de formatos SAT al sistema contable
- Procesamiento FEL / RTU / PDF / XML
- Clasificación de gastos
- Bienes y servicios
- Deducibilidad ISR
- Crédito fiscal IVA
- Revisión tributaria
- Conciliaciones
- Libros
- Reportes
- Preparación de borradores de declaraciones
- Audit trail y revisión humana

## Declaraciones previstas

- SAT-1311
- SAT-1331
- SAT-1361
- SAT-1608
- SAT-2046
- SAT-2237

Las declaraciones generadas por el sistema deben considerarse **borradores para revisión humana**.

## Integridad de datos

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

## Build de Windows

El objetivo del pipeline es:

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

## Estado del proyecto

Actualmente el proyecto se encuentra en fase de **productización Desktop y empaquetado para Windows**.

## Aviso

America Audit es una herramienta de apoyo contable y tributario. Los resultados, clasificaciones, cálculos y borradores de declaraciones deben ser revisados por personal responsable antes de su presentación o uso oficial.

## Versión

**America Audit Desktop 1.0.0**
