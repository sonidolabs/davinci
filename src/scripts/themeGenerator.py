import json

# Secondary Button & TitleBar Inactive Foreground
dark1 = '#2F313C'

# ActivityBar & Editor
dark2 = '#191A20'

# SideBar & Terminal
dark3 = '#131418'

# Inputs & Menus
dark4 = '#202128'

# Dropdowns & Others
dark5 = '#202128'

mainColor = '#F4AFD2'
mainColorHover = '#F4AFD2AA'
foreground = '#9D9AB1'
bgListHover = '#ffffff10'
badgesForeground = '#101010'
transparent = '#00000000'
inactiveIcons = '#4A4D69'
border = '#38374E88'

data = {
  "$schema": "vscode://schemas/color-theme",
  "name": "Davinci",
  "author": "Gabriel Batista",
  "type": "dark",
  "semanticClass": "theme.davinci",
  "semanticHighlighting": True,
  "maintainers": [
    "Gabriel Batista <gabriel3atista@gmail.com>"
    ],
  "davinci": {
    "base": [
        "#282A36",
        "#F8F8F2",
        "#44475A",
        "#6272A4",
        "#66DAFF",
        "#13FBA7",
        "#FF9960",
        "#F9507F",
        "#66DAFF",
        "#FF4B61",
        "#FFE176"
    ],
    "ansi": [
        "#21222C",
        "#FF4B61",
        "#13FBA7",
        "#FFE176",
        "#66DAFF",
        "#F9507F",
        "#66DAFF",
        "#F8F8F2",
        "#6272A4",
        "#FF6E6E",
        "#69FF94",
        "#FFFFA5",
        "#D6ACFF",
        "#FF92DF",
        "#A4FFFF",
        "#FFFFFF"
    ],
  },
  "colors": {
    "foreground": foreground,
    "focusBorder": transparent,
    "selection.background": dark1,
    "scrollbar.shadow": transparent,
    "activityBar.foreground": mainColor,
    "activityBar.background": dark2,
    "activityBar.dropBorder": "#ffffff",
    "activityBar.inactiveForeground": inactiveIcons,
    "activityBarBadge.background": mainColor,
    "activityBarBadge.foreground": badgesForeground,
    "activityBar.border": border,
    "activityBar.activeBackground": "#36394700",
    "sideBar.background": dark3,
    "sideBar.foreground": foreground,
    "sideBarSectionHeader.background": dark2,
    "sideBarSectionHeader.foreground": "#ffffff",
    "sideBarSectionHeader.border": transparent,
    "sideBarTitle.foreground": mainColor,
    "sideBar.border": border,
    "list.inactiveSelectionBackground": "#ffffff10",
    "list.inactiveSelectionForeground": "#ffffff",
    "list.hoverBackground": "#ffffff10",
    "list.hoverForeground": "#ffffff",
    "list.activeSelectionBackground": "#ffffff10",
    "list.activeSelectionForeground": "#ffffff",
    "tree.indentGuidesStroke": border,
    "list.dropBackground": "#36394780",
    "list.highlightForeground": mainColor,
    "list.focusBackground": border,
    "list.focusForeground": "#ffffff",
    "listFilterWidget.background": "#431b24",
    "listFilterWidget.outline": transparent,
    "listFilterWidget.noMatchesOutline": transparent,
    "statusBar.foreground": foreground,
    "statusBar.background": dark2,
    "statusBarItem.hoverBackground": transparent,
    "statusBar.border": border,
    "statusBar.debuggingBackground": mainColor,
    "statusBar.debuggingForeground": badgesForeground,
    "statusBar.debuggingBorder": transparent,
    "statusBar.noFolderBackground": dark2,
    "statusBar.noFolderForeground": foreground,
    "statusBar.noFolderBorder": transparent,
    "statusBarItem.remoteBackground": mainColor,
    "statusBarItem.remoteForeground": badgesForeground,
    "titleBar.activeBackground": dark2,
    "titleBar.activeForeground": foreground,
    "titleBar.inactiveBackground": dark2,
    "titleBar.inactiveForeground": dark1,
    "titleBar.border": border,
    "menubar.selectionForeground": "#ffffff",
    "menubar.selectionBackground": "#ffffff10",
    "menubar.selectionBorder": transparent,
    "menu.foreground": foreground,
    "menu.background": dark4,
    "menu.selectionForeground": "#ffffff",
    "menu.selectionBackground": "#ffffff10",
    "menu.selectionBorder": transparent,
    "menu.separatorBackground": border,
    "menu.border": transparent,
    "button.background": mainColor,
    "button.foreground": badgesForeground,
    "button.hoverBackground": mainColorHover,
    "button.secondaryForeground": "#ffffff",
    "button.secondaryBackground": border,
    "button.secondaryHoverBackground": dark1,
    "input.background": dark2,
    "input.border": transparent,
    "input.foreground": "#ffffff",
    "inputOption.activeBackground": dark1,
    "inputOption.activeBorder": transparent,
    "inputOption.activeForeground": "#ffffff",
    "input.placeholderForeground": foreground,
    "textLink.foreground": "#2e7ff8",
    "editor.background": dark2,
    "editor.foreground": "#ffffff",
    "editorLineNumber.foreground": foreground,
    "editorCursor.foreground": mainColor,
    "editorCursor.background": "#000000",
    "editor.selectionBackground": dark1,
    "editor.inactiveSelectionBackground": "#ffffff10",
    "editorWhitespace.foreground": "#ffffff29",
    "editor.selectionHighlightBackground": dark1,
    "editor.selectionHighlightBorder": "#495f7700",
    "editor.findMatchBackground": "#ea5e0077",
    "editor.findMatchBorder": transparent,
    "editor.findMatchHighlightBackground": dark1,
    "editor.findMatchHighlightBorder": transparent,
    "editor.findRangeHighlightBackground": "#3a3d4166",
    "editor.findRangeHighlightBorder": transparent,
    "editor.rangeHighlightBackground": transparent,
    "editor.rangeHighlightBorder": transparent,
    "editor.hoverHighlightBackground": "#264f78a1",
    "editor.wordHighlightStrongBackground": "#004972b7",
    "editor.wordHighlightBackground": "#5757578b",
    "editor.lineHighlightBackground": dark1,
    "editor.lineHighlightBorder": transparent,
    "editorLineNumber.activeForeground": "#ffffff",
    "editorLink.activeForeground": "#57a0fd",
    "editorIndentGuide.background": border,
    "editorIndentGuide.activeBackground": dark1,
    "editorRuler.foreground": border,
    "editorBracketMatch.background": "#0064001a",
    "editorBracketMatch.border": dark1,
    "editor.foldBackground": transparent,
    "editorOverviewRuler.background": transparent,
    "editorOverviewRuler.border": "#7f7f7f00",
    "editorError.foreground": "#f9215d",
    "editorError.background": "#f9215d1a",
    "editorError.border": transparent,
    "editorWarning.foreground": "#d9b823",
    "editorWarning.background": "#cba8381a",
    "editorWarning.border": transparent,
    "editorInfo.foreground": "#75beff",
    "editorInfo.background": "#4490bf1a",
    "editorInfo.border": "#4490BF00",
    "editorGutter.background": dark2,
    "editorGutter.modifiedBackground": "#57a0fd",
    "editorGutter.addedBackground": "#57fdaf",
    "editorGutter.deletedBackground": mainColor,
    "editorGutter.foldingControlForeground": foreground,
    "editorCodeLens.foreground": foreground,
    "editorGroup.border": border,
    "diffEditor.insertedTextBackground": "#57fdaf26",
    "diffEditor.insertedTextBorder": transparent,
    "diffEditor.removedTextBackground": "#fd577e26",
    "diffEditor.removedTextBorder": transparent,
    "diffEditor.border": transparent,
    "panel.background": dark3,
    "panel.border": mainColor,
    "panelTitle.activeBorder": mainColor,
    "panelTitle.activeForeground": "#ffffff",
    "panelTitle.inactiveForeground": foreground,
    "badge.background": mainColor,
    "badge.foreground": badgesForeground,
    "terminal.foreground": foreground,
    "terminal.selectionBackground": dark1,
    "terminalCursor.background": dark3,
    "terminalCursor.foreground": "#ffffff",
    "terminal.border": border,
    "terminal.ansiBlack": "#000000",
    "terminal.ansiBlue": "#2472c8",
    "terminal.ansiBrightBlack": "#666666",
    "terminal.ansiBrightBlue": "#3b8eea",
    "terminal.ansiBrightCyan": "#29b8db",
    "terminal.ansiBrightGreen": "#23d18b",
    "terminal.ansiBrightMagenta": "#d670d6",
    "terminal.ansiBrightRed": "#f14c4c",
    "terminal.ansiBrightWhite": "#e5e5e5",
    "terminal.ansiBrightYellow": "#f5f543",
    "terminal.ansiCyan": "#21d3ff",
    "terminal.ansiGreen": "#13FBA7",
    "terminal.ansiMagenta": "#f93778",
    "terminal.ansiRed": "#cd3131",
    "terminal.ansiWhite": "#ffffff",
    "terminal.ansiYellow": "#e5e510",
    "breadcrumb.background": dark2,
    "breadcrumb.foreground": foreground,
    "breadcrumb.focusForeground": "#ffffff",
    "editorGroupHeader.border": "#ff005400",
    "editorGroupHeader.tabsBackground": dark3,
    "editorGroupHeader.tabsBorder": transparent,
    "tab.activeForeground": "#ffffff",
    "tab.border": transparent,
    "tab.activeBackground": dark2,
    "tab.activeBorder": transparent,
    "tab.activeBorderTop": mainColor,
    "tab.inactiveBackground": dark3,
    "tab.inactiveForeground": foreground,
    "tab.hoverBackground": dark2,
    "tab.hoverForeground": "#ffffff",
    "tab.hoverBorder": transparent,
    "scrollbarSlider.background": dark1,
    "scrollbarSlider.hoverBackground": "#ffffff30",
    "scrollbarSlider.activeBackground": "#ffffff40",
    "progressBar.background": mainColor,
    "widget.shadow": "#00000042",
    "editorWidget.foreground": foreground,
    "editorWidget.background": dark4,
    "editorWidget.resizeBorder": mainColor,
    "pickerGroup.border": "#30306b00",
    "pickerGroup.foreground": mainColor,
    "debugToolBar.background": dark2,
    "debugToolBar.border": border,
    "notifications.foreground": foreground,
    "notifications.background": dark2,
    "notificationToast.border": border,
    "notificationsErrorIcon.foreground": "#f9215d",
    "notificationsWarningIcon.foreground": "#f9cd21",
    "notificationsInfoIcon.foreground": "#21a3f9",
    "notificationCenter.border": border,
    "notificationCenterHeader.foreground": "#ffffff",
    "notificationCenterHeader.background": dark4,
    "notifications.border": border,
    "gitDecoration.addedResourceForeground": "#94d6a0",
    "gitDecoration.conflictingResourceForeground": "#8282ee",
    "gitDecoration.deletedResourceForeground": "#e45c44",
    "gitDecoration.ignoredResourceForeground": "#5D627A",
    "gitDecoration.modifiedResourceForeground": "#f3cc92",
    "gitDecoration.stageDeletedResourceForeground": "#e65d45",
    "gitDecoration.stageModifiedResourceForeground": "#f1cb92",
    "gitDecoration.submoduleResourceForeground": "#8ec8ff",
    "gitDecoration.untrackedResourceForeground": "#81eea7",
    "editorMarkerNavigation.background": dark2,
    "editorMarkerNavigationError.background": "#f9215d80",
    "editorMarkerNavigationWarning.background": "#f9b92180",
    "editorMarkerNavigationInfo.background": "#21b2f980",
    "merge.currentHeaderBackground": "#215a45",
    "merge.currentContentBackground": "#264137",
    "merge.incomingHeaderBackground": "#213a5a",
    "merge.incomingContentBackground": "#263241",
    "merge.commonHeaderBackground": "#4f3434",
    "merge.commonContentBackground": "#282828",
    "editorSuggestWidget.background": dark4,
    "editorSuggestWidget.border": border,
    "editorSuggestWidget.foreground": foreground,
    "editorSuggestWidget.highlightForeground": mainColor,
    "editorSuggestWidget.selectedBackground": dark1,
    "editorHoverWidget.foreground": foreground,
    "editorHoverWidget.background": dark2,
    "editorHoverWidget.border": border,
    "peekView.border": "#007acc",
    "peekViewEditor.background": "#001f33",
    "peekViewEditorGutter.background": "#001f33",
    "peekViewEditor.matchHighlightBackground": "#ff8f0099",
    "peekViewEditor.matchHighlightBorder": "#ee931e",
    "peekViewResult.background": dark2,
    "peekViewResult.fileForeground": foreground,
    "peekViewResult.lineForeground": foreground,
    "peekViewResult.matchHighlightBackground": "#ea5c004d",
    "peekViewResult.selectionBackground": border,
    "peekViewResult.selectionForeground": "#ffffff",
    "peekViewTitle.background": dark2,
    "peekViewTitleDescription.foreground": foreground,
    "peekViewTitleLabel.foreground": "#ffffff",
    "icon.foreground": mainColor,
    "checkbox.background": border,
    "checkbox.foreground": "#ffffff",
    "checkbox.border": transparent,
    "dropdown.background": dark5,
    "dropdown.foreground": "#ffffff",
    "dropdown.border": transparent,
    "minimapGutter.addedBackground": "#57fdaf",
    "minimapGutter.modifiedBackground": "#57a0fd",
    "minimapGutter.deletedBackground": "#f9215d",
    "minimap.findMatchHighlight": "#515c6a",
    "minimap.selectionHighlight": "#5d627a4e",
    "minimap.errorHighlight": "#f9215d",
    "minimap.warningHighlight": "#d9b823",
    "minimap.background": dark2,
    "sideBar.dropBackground": "#36394780",
    "editorGroup.emptyBackground": dark2,
    "panelSection.border": "#964d4d59",
    "statusBarItem.activeBackground": "#FFFFFF25",
    "settings.headerForeground": mainColor,
    "settings.focusedRowBackground": "#ffffff07",
    "walkThrough.embeddedEditorBackground": "#00000050",
    "breadcrumb.activeSelectionForeground": "#ffffff",
    "editorGutter.commentRangeForeground": foreground,
    "debugExceptionWidget.background": border,
    "debugExceptionWidget.border": dark1
  },
  "tokenColors": [
    {
        "scope": [
            "emphasis"
        ],
        "settings": {
            "fontStyle": "italic"
        }
    },
    {
        "scope": [
            "strong"
        ],
        "settings": {
            "fontStyle": "bold"
        }
    },
    {
        "scope": [
            "header"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "scope": [
            "meta.diff",
            "meta.diff.header"
        ],
        "settings": {
            "foreground": "#6272A4"
        }
    },
    {
        "scope": "punctuation.accessor.js",
        "settings": {
            "foreground": "#FF4B61"
        }
    },
    {
        "scope": [
            "markup.inserted"
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "scope": [
            "markup.deleted"
        ],
        "settings": {
            "foreground": "#FF4B61"
        }
    },
    {
        "scope": [
            "markup.changed"
        ],
        "settings": {
            "foreground": "#FF9960"
        }
    },
    {
        "scope": [
            "invalid"
        ],
        "settings": {
            "foreground": "#FF4B61",
            "fontStyle": "underline italic"
        }
    },
    {
        "scope": [
            "invalid.deprecated"
        ],
        "settings": {
            "foreground": "#F8F8F2",
            "fontStyle": "underline italic"
        }
    },
    {
        "scope": [
            "entity.name.filename"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "scope": [
            "markup.error"
        ],
        "settings": {
            "foreground": "#FF4B61"
        }
    },
    {
        "name": "Underlined markup",
        "scope": [
            "markup.underline"
        ],
        "settings": {
            "fontStyle": "underline"
        }
    },
    {
        "name": "Bold markup",
        "scope": [
            "markup.bold"
        ],
        "settings": {
            "fontStyle": "bold",
            "foreground": "#FF9960"
        }
    },
    {
        "name": "Markup headings",
        "scope": [
            "markup.heading"
        ],
        "settings": {
            "fontStyle": "bold",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Markup italic",
        "scope": [
            "markup.italic"
        ],
        "settings": {
            "foreground": "#FFE176",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Bullets, lists (prose)",
        "scope": [
            "beginning.punctuation.definition.list.markdown",
            "beginning.punctuation.definition.quote.markdown",
            "punctuation.definition.link.restructuredtext"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Inline code (prose)",
        "scope": [
            "markup.inline.raw",
            "markup.raw.restructuredtext"
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Links (prose)",
        "scope": [
            "markup.underline.link",
            "markup.underline.link.image"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Link text, image alt text (prose)",
        "scope": [
            "meta.link.reference.def.restructuredtext",
            "punctuation.definition.directive.restructuredtext",
            "string.other.link.description",
            "string.other.link.title"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Blockquotes (prose)",
        "scope": [
            "entity.name.directive.restructuredtext",
            "markup.quote"
        ],
        "settings": {
            "foreground": "#FFE176",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Horizontal rule (prose)",
        "scope": [
            "meta.separator.markdown"
        ],
        "settings": {
            "foreground": "#6272A4"
        }
    },
    {
        "name": "Code blocks",
        "scope": [
            "fenced_code.block.language",
            "markup.raw.inner.restructuredtext",
            "markup.fenced_code.block.markdown punctuation.definition.markdown"
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Prose constants",
        "scope": [
            "punctuation.definition.constant.restructuredtext"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Braces in markdown headings",
        "scope": [
            "markup.heading.markdown punctuation.definition.string.begin",
            "markup.heading.markdown punctuation.definition.string.end"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Braces in markdown paragraphs",
        "scope": [
            "meta.paragraph.markdown punctuation.definition.string.begin",
            "meta.paragraph.markdown punctuation.definition.string.end",
            "meta.object-literal.key",
            "text.html"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "Braces in markdown blockquotes",
        "scope": [
            "markup.quote.markdown meta.paragraph.markdown punctuation.definition.string.begin",
            "markup.quote.markdown meta.paragraph.markdown punctuation.definition.string.end"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "User-defined class names",
        "scope": [
            "entity.name.type.class",
            "entity.name.class"
        ],
        "settings": {
            "foreground": "#66DAFF",
            "fontStyle": "normal"
        }
    },
    {
        "name": "this, super, self, etc.",
        "scope": [
            "keyword.expressions-and-types.swift",
            "keyword.other.this",
            "variable.language",
            "variable.language punctuation.definition.variable.php",
            "variable.other.readwrite.instance.ruby",
            "variable.parameter.function.language.special"
        ],
        "settings": {
            "foreground": "#d466ff",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Inherited classes",
        "scope": [
            "entity.other.inherited-class"
        ],
        "settings": {
            "fontStyle": "italic",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Comments",
        "scope": [
            "comment",
            "punctuation.definition.comment",
            "unused.comment",
            "wildcard.comment"
        ],
        "settings": {
            "foreground": "#6272A4"
        }
    },
    {
        "name": "JSDoc-style keywords",
        "scope": [
            "comment keyword.codetag.notation",
            "comment.block.documentation keyword",
            "comment.block.documentation storage.type.class",
            "punctuation.accessor.optional.ts"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "JSDoc-style types",
        "scope": [
            "comment.block.documentation entity.name.type"
        ],
        "settings": {
            "foreground": "#66DAFF",
            "fontStyle": "italic"
        }
    },
    {
        "name": "JSDoc-style type brackets",
        "scope": [
            "comment.block.documentation entity.name.type punctuation.definition.bracket"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "JSDoc-style comment parameters",
        "scope": [
            "comment.block.documentation variable"
        ],
        "settings": {
            "foreground": "#FF9960",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Constants",
        "scope": [
            "constant",
            "variable.other.constant"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Constant escape sequences",
        "scope": [
            "constant.character.escape",
            "constant.character.string.escape",
            "constant.regexp",
            ""
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "HTML tags",
        "scope": [
            "entity.name.tag"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "CSS attribute parent selectors ('&')",
        "scope": [
            "entity.other.attribute-name.parent-selector"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "HTML/CSS attribute names",
        "scope": [
            "entity.other.attribute-name"
        ],
        "settings": {
            "foreground": "#13FBA7",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Function names",
        "scope": [
            "entity.name.function",
            "meta.function-call.object",
            "meta.function-call.php",
            "meta.function-call.static",
            "meta.method-call.java meta.method",
            "meta.method.groovy",
            "support.function.any-method.lua",
            "keyword.operator.function.infix"
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Function parameters",
        "scope": [
            "entity.name.variable.parameter",
            "meta.at-rule.function variable",
            "meta.at-rule.mixin variable",
            "meta.function.arguments variable.other.php",
            "meta.selectionset.graphql meta.arguments.graphql variable.arguments.graphql",
            "variable.parameter"
        ],
        "settings": {
            "fontStyle": "italic",
            "foreground": "#FF9960"
        }
    },
    {
        "name": "Decorators",
        "scope": [
            "meta.decorator variable.other.readwrite",
            "meta.decorator variable.other.property"
        ],
        "settings": {
            "foreground": "#13FBA7",
            "fontStyle": "italic"
        }
    },
    {
        "name": "Decorator Objects",
        "scope": [
            "meta.decorator variable.other.object",
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Keywords",
        "scope": [
            "keyword",
            "punctuation.definition.keyword"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Keyword \"new\"",
        "scope": [
            "keyword.control.new",
            "keyword.operator.new"
        ],
        "settings": {
            "fontStyle": "bold"
        }
    },
    {
        "name": "Generic selectors (CSS/SCSS/Less/Stylus)",
        "scope": [
            "meta.selector"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Language Built-ins",
        "scope": [
            "support"
        ],
        "settings": {
            "fontStyle": "italic",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Built-in magic functions and constants",
        "scope": [
            "support.function.magic",
            "support.variable",
            "variable.other.predefined"
        ],
        "settings": {
            "fontStyle": "regular",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Built-in functions / properties",
        "scope": [
            "support.function",
            "support.type.property-name"
        ],
        "settings": {
            "fontStyle": "regular",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Separators (key/value, namespace, inheritance, pointer, hash, slice, etc)",
        "scope": [
            "constant.other.symbol.hashkey punctuation.definition.constant.ruby",
            "entity.other.attribute-name.placeholder punctuation",
            "entity.other.attribute-name.pseudo-class punctuation",
            "entity.other.attribute-name.pseudo-element punctuation",
            "meta.group.double.toml",
            "meta.group.toml",
            "meta.object-binding-pattern-variable punctuation.destructuring",
            "punctuation.colon.graphql",
            "punctuation.definition.block.scalar.folded.yaml",
            "punctuation.definition.block.scalar.literal.yaml",
            "punctuation.definition.block.sequence.item.yaml",
            "punctuation.definition.entity.other.inherited-class",
            "punctuation.function.swift",
            "punctuation.separator.dictionary.key-value",
            "punctuation.separator.hash",
            "punctuation.separator.inheritance",
            "punctuation.separator.key-value",
            "punctuation.separator.key-value.mapping.yaml",
            "punctuation.separator.namespace",
            "punctuation.separator.pointer-access",
            "punctuation.separator.slice",
            "string.unquoted.heredoc punctuation.definition.string",
            "support.other.chomping-indicator.yaml",
            "punctuation.separator.annotation"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Brackets, braces, parens, etc.",
        "scope": [
            "keyword.operator.other.powershell",
            "keyword.other.statement-separator.powershell",
            "meta.brace.round",
            "meta.function-call punctuation",
            "punctuation.definition.arguments.begin",
            "punctuation.definition.arguments.end",
            "punctuation.definition.entity.begin",
            "punctuation.definition.entity.end",
            "punctuation.definition.tag.cs",
            "punctuation.definition.type.begin",
            "punctuation.definition.type.end",
            "punctuation.section.scope.begin",
            "punctuation.section.scope.end",
            "punctuation.terminator.expression.php",
            "storage.type.generic.java",
            "string.template meta.brace",
            "string.template punctuation.accessor",
            "punctuation.definition.tag.end.html",
            "punctuation.definition.tag.begin.html",
            "source"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "Variable interpolation operators",
        "scope": [
            "meta.string-contents.quoted.double punctuation.definition.variable",
            "punctuation.definition.interpolation.begin",
            "punctuation.definition.interpolation.end",
            "punctuation.definition.template-expression.begin",
            "punctuation.definition.template-expression.end",
            "punctuation.section.embedded.begin",
            "punctuation.section.embedded.coffee",
            "punctuation.section.embedded.end",
            "punctuation.section.embedded.end source.php",
            "punctuation.section.embedded.end source.ruby",
            "punctuation.definition.variable.makefile"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Keys (serializable languages)",
        "scope": [
            "entity.name.function.target.makefile",
            "entity.name.section.toml",
            "entity.name.tag.yaml",
            "variable.other.key.toml"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Dates / timestamps (serializable languages)",
        "scope": [
            "constant.other.date",
            "constant.other.timestamp"
        ],
        "settings": {
            "foreground": "#FF9960"
        }
    },
    {
        "name": "YAML aliases",
        "scope": [
            "variable.other.alias.yaml"
        ],
        "settings": {
            "fontStyle": "italic underline",
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Storage",
        "scope": [
            "storage",
            "meta.implementation storage.type.objc",
            "meta.interface-or-protocol storage.type.objc",
            "source.groovy storage.type.def"
        ],
        "settings": {
            "fontStyle": "regular",
            "foreground": "#F9507F"
        }
    },
    {
        "name": "Types",
        "scope": [
            "entity.name.type",
            "keyword.primitive-datatypes.swift",
            "keyword.type.cs",
            "meta.protocol-list.objc",
            "meta.return-type.objc",
            "source.go storage.type",
            "source.groovy storage.type",
            "source.java storage.type",
            "source.powershell entity.other.attribute-name",
            "storage.class.std.rust",
            "storage.type.attribute.swift",
            "storage.type.c",
            "storage.type.core.rust",
            "storage.type.cs",
            "storage.type.groovy",
            "storage.type.objc",
            "storage.type.php",
            "storage.type.haskell",
            "storage.type.ocaml"
        ],
        "settings": {
            "fontStyle": "italic",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Generics, templates, and mapped type declarations",
        "scope": [
            "entity.name.type.type-parameter",
            "meta.indexer.mappedtype.declaration entity.name.type",
            "meta.type.parameters entity.name.type"
        ],
        "settings": {
            "foreground": "#FF9960"
        }
    },
    {
        "name": "Modifiers",
        "scope": [
            "storage.modifier"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "RegExp string",
        "scope": [
            "string.regexp",
            "constant.other.character-class.set.regexp",
            "constant.character.escape.backslash.regexp"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "Non-capture operators",
        "scope": [
            "punctuation.definition.group.capture.regexp"
        ],
        "settings": {
            "foreground": "#F9507F"
        }
    },
    {
        "name": "RegExp start and end characters",
        "scope": [
            "string.regexp punctuation.definition.string.begin",
            "string.regexp punctuation.definition.string.end"
        ],
        "settings": {
            "foreground": "#FF4B61"
        }
    },
    {
        "name": "Character group",
        "scope": [
            "punctuation.definition.character-class.regexp"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Capture groups",
        "scope": [
            "punctuation.definition.group.regexp"
        ],
        "settings": {
            "foreground": "#FF9960"
        }
    },
    {
        "name": "Assertion operators",
        "scope": [
            "punctuation.definition.group.assertion.regexp",
            "keyword.operator.negation.regexp"
        ],
        "settings": {
            "foreground": "#FF4B61"
        }
    },
    {
        "name": "Positive lookaheads",
        "scope": [
            "meta.assertion.look-ahead.regexp"
        ],
        "settings": {
            "foreground": "#13FBA7"
        }
    },
    {
        "name": "Strings",
        "scope": [
            "string"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "String quotes (temporary vscode fix)",
        "scope": [
            "punctuation.definition.string.begin",
            "punctuation.definition.string.end"
        ],
        "settings": {
            "foreground": "#E9F284"
        }
    },
    {
        "name": "Property quotes (temporary vscode fix)",
        "scope": [
            "punctuation.support.type.property-name.begin",
            "punctuation.support.type.property-name.end"
        ],
        "settings": {
            "foreground": "#8BE9FE"
        }
    },
    {
        "name": "Docstrings",
        "scope": [
            "string.quoted.docstring.multi",
            "string.quoted.docstring.multi.python punctuation.definition.string.begin",
            "string.quoted.docstring.multi.python punctuation.definition.string.end",
            "string.quoted.docstring.multi.python constant.character.escape"
        ],
        "settings": {
            "foreground": "#6272A4"
        }
    },
    {
        "name": "Variables and object properties",
        "scope": [
            "variable",
            "constant.other.key.perl",
            "support.variable.property",
            "variable.other.constant.js",
            "variable.other.constant.ts",
            "variable.other.constant.tsx"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "Destructuring / aliasing reference name (LHS)",
        "scope": [
            "meta.import variable.other.readwrite",
            "meta.variable.assignment.destructured.object.coffee variable"
        ],
        "settings": {
            "fontStyle": "italic",
            "foreground": "#FF9960"
        }
    },
    {
        "name": "Destructuring / aliasing variable name (RHS)",
        "scope": [
            "meta.import variable.other.readwrite.alias",
            "meta.export variable.other.readwrite.alias",
            "meta.variable.assignment.destructured.object.coffee variable variable"
        ],
        "settings": {
            "fontStyle": "normal",
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "GraphQL keys",
        "scope": [
            "meta.selectionset.graphql variable"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "GraphQL function arguments",
        "scope": [
            "meta.selectionset.graphql meta.arguments variable"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "GraphQL fragment name (definition)",
        "scope": [
            "entity.name.fragment.graphql",
            "variable.fragment.graphql"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Edge cases (foreground color resets)",
        "scope": [
            "constant.other.symbol.hashkey.ruby",
            "keyword.operator.dereference.java",
            "keyword.operator.navigation.groovy",
            "meta.scope.for-loop.shell punctuation.definition.string.begin",
            "meta.scope.for-loop.shell punctuation.definition.string.end",
            "meta.scope.for-loop.shell string",
            "storage.modifier.import",
            "punctuation.section.embedded.begin.tsx",
            "punctuation.section.embedded.end.tsx",
            "punctuation.section.embedded.begin.jsx",
            "punctuation.section.embedded.end.jsx",
            "punctuation.separator.list.comma.css",
            "constant.language.empty-list.haskell"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "Shell variables prefixed with \"$\" (edge case)",
        "scope": [
            "source.shell variable.other"
        ],
        "settings": {
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Powershell constants mistakenly scoped to `support`, rather than `constant` (edge)",
        "scope": [
            "support.constant"
        ],
        "settings": {
            "fontStyle": "normal",
            "foreground": "#66DAFF"
        }
    },
    {
        "name": "Makefile prerequisite names",
        "scope": [
            "meta.scope.prerequisites.makefile"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "SCSS attibute selector strings",
        "scope": [
            "meta.attribute-selector.scss"
        ],
        "settings": {
            "foreground": "#FFE176"
        }
    },
    {
        "name": "SCSS attribute selector brackets",
        "scope": [
            "punctuation.definition.attribute-selector.end.bracket.square.scss",
            "punctuation.definition.attribute-selector.begin.bracket.square.scss"
        ],
        "settings": {
            "foreground": "#F8F8F2"
        }
    },
    {
        "name": "Haskell Pragmas",
        "scope": [
            "meta.preprocessor.haskell"
        ],
        "settings": {
            "foreground": "#6272A4"
        }
    },
    {
        "name": "Log file error",
        "scope": [
            "log.error"
        ],
        "settings": {
            "foreground": "#FF4B61",
            "fontStyle": "bold"
        }
    },
    {
        "name": "Log file warning",
        "scope": [
            "log.warning"
        ],
        "settings": {
            "foreground": "#FFE176",
            "fontStyle": "bold"
        }
    }
  ]
}

output_path = "./src/themes/teste.json"

with open(output_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Theme generated and saved in {output_path}")