# Templates

## Filosofía de Código

### Principios

1. **Atomic Design** — Componentes pequeños, de responsabilidad única
2. **DRY** — No repetiras código; extract a componentes
3. **Consistencia** — Nombres claros y predictibles
4. **Flexibilidad** — Includes sobre herencia cuando sea posible

### Estructura

```
templates/
├── base.html              # Template raíz
├── account/               # Autenticación allauth
├── dashboard/             # Vistas del dashboard
├── components/           # Componentes reutilizables
│   ├── ui/
│   │   ├── button.html
│   │   ├── input.html
│   │   ├── link.html
│   │   └── ...
│   └── error_block.html
└── admin/                 # Templates Django admin
```

### Componentes

** atomic design: cada componente hace una cosa**

```html
{% include "components/ui/button.html" with text="Submit" %}
```

**Reglas:**
- Un componente = un archivo
- Nombres en kebab-case
- Styles inline (Tailwind) — no external CSS files
- No lógica compleja en templates

### Estilos

**Tailwind CSS** — clases utility directamente en HTML

```html
<div class="bg-gray-900 text-white rounded-lg">
```

**Nomenclatura de colores:**
- `gray-900` — Negro
- `gray-500` — Gray medio
- `red-500` — Errores

### Herencia

```
base.html
    └── account/login.html
    └── dashboard/home.html
```

Evitar多层 herencia (más de 2 niveles).

### Mejores Prácticas

| Hacer | No hacer |
|-------|---------|
| Usar `{% include %}` para componentes | Copiar código |
| Mantener componentes pequeños | Componentes gigante |
| Nombres descriptivos | `partial_1.html` |
| Tailwind classes | CSS externo |
| `{% block %}` para contenido | `{% include %}` con lógica |

### Beispiel

```html
{% extends "base.html" %}

{% block title %}Sign In{% endblock %}

{% block content %}
{% include "account/login.html" %}
{% endblock %}
```

## Contribuir

1. Crear componente si se usa 2+ veces
2. Mantener simple — un componente, una cosa
3. Usar estilos existentes antes de crear nuevos
4. Documentar con comments si lógica es compleja

## Backlog Futuro

- [ ] Agregar una suite de visual regression para capturar screenshots por ruta, tema y breakpoint
- [ ] Mantener una baseline aprobada para detectar regresiones visuales en CI
