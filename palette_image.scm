(define (script-fu-palette-image)
  ; Create a new image: 255 pixels wide, 1 pixel high, RGB
  (let* ((img (car (gimp-image-new 255 1 RGB)))
         (drawable (car (gimp-layer-new img 255 1 RGB-IMAGE "Palette Layer" 100 LAYER-MODE-NORMAL)))
         (colors
          '(
            (27 27 27)    ; Black
            (17 29 37)    ; NightAzure
            (5 29 50)     ; ShadowCerulean
            (46 56 71)    ; DarkCerulean
            (54 54 77)    ; DarkCobalt
            (65 52 65)    ; DarkBerry
            (73 47 73)    ; DarkViolet
            (76 42 91)    ; DarkLilac
            (99 16 99)    ; StrongViolet
            (95 30 77)    ; StrongMagenta
            (110 13 54)   ; StrongFuchsia
            (105 26 35)   ; StrongCherry
            (90 41 35)    ; DarkRed
            (79 48 35)    ; DarkOrange
            (73 50 50)    ; DarkRose
            (82 44 55)    ; DarkFuchsia
            (60 4 27)     ; ShadowFuchsia
            (46 17 38)    ; NightBerry
            (43 21 27)    ; NightFuchsia
            (37 25 20)    ; NightOrange
            (47 20 3)     ; ShadowOrange
            (63 3 3)      ; ShadowRed
            (115 12 12)   ; StrongRed
            (171 23 23)   ; DeepRed
            (158 44 57)   ; HotCherry
            (131 68 68)   ; SilkCherry
            (110 78 82)   ; OxideRose
            (110 79 67)   ; SilkOrange
            (100 83 67)   ; SilkMustard
            (117 78 42)   ; HotSepia
            (112 81 22)   ; DeepMustard
            (99 85 42)    ; HotTan
            (88 88 56)    ; SilkYellow
            (89 89 22)    ; DeepYellow
            (64 95 42)    ; HotMoss
            (22 100 22)   ; DeepGreen
            (11 65 11)    ; StrongGreen
            (44 60 34)    ; DarkGreen
            (57 57 34)    ; DarkYellow
            (58 58 11)    ; StrongYellow
            (73 52 11)    ; StrongMustard
            (65 54 35)    ; DarkMustard
            (36 26 3)     ; ShadowMustard
            (29 29 3)     ; ShadowYellow
            (19 30 19)    ; NightGreen
            (4 31 31)     ; ShadowTurquoise
            (44 58 58)    ; DarkTurquoise
            (62 62 62)    ; DarkGrey
            (79 87 93)    ; OxideAzure
            (99 99 99)    ; OxideGrey
            (87 87 77)    ; OxideYellow
            (77 90 77)    ; OxideGreen
            (67 93 67)    ; SilkMint
            (58 93 83)    ; SilkTeal
            (25 96 96)    ; DeepTurquoise
            (26 94 110)   ; DeepSlate
            (27 92 125)   ; DeepAzure
            (30 87 154)   ; DeepCerulean
            (67 83 143)   ; SilkCobalt
            (73 87 111)   ; SilkCerulean
            (84 84 114)   ; OxideBlue
            (99 80 99)    ; OxideViolet
            (111 73 111)  ; SilkBerry
            (115 66 136)  ; SilkLilac
            (93 70 162)   ; SilkLavender
            (109 37 213)  ; DeepLavender
            (134 33 179)  ; DeepLilac
            (148 30 148)  ; DeepViolet
            (143 49 118)  ; HotMagenta
            (136 60 97)   ; SilkMagenta
            (165 25 84)   ; DeepFuchsia
            (190 83 117)  ; WarmFuchsia
            (202 67 138)  ; WarmMagenta
            (224 38 116)  ; Fuchsia
            (227 36 90)   ; Rose
            (197 81 92)   ; WarmCherry
            (230 35 64)   ; Cherry
            (232 35 35)   ; Red
            (200 81 61)   ; WarmRed
            (168 101 94)  ; StaleRed
            (163 105 79)  ; WarmOrange
            (144 113 94)  ; StaleSepia
            (141 115 79)  ; WarmMustard
            (127 119 94)  ; StaleTan
            (121 121 79)  ; WarmYellow
            (105 125 93)  ; StaleMoss
            (81 129 107)  ; WarmViridian
            (37 133 117)  ; Teal
            (36 134 98)   ; Viridian
            (34 136 73)   ; Mint
            (34 137 33)   ; Green
            (90 130 60)   ; WarmMoss
            (123 123 34)  ; Yellow
            (139 117 34)  ; Tan
            (153 112 34)  ; Mustard
            (168 105 34)  ; Sepia
            (183 95 34)   ; Orange
            (234 123 47)  ; VividOrange
            (208 137 80)  ; LightSepia
            (209 135 103) ; LightOrange
            (184 145 122) ; PaleSepia
            (166 151 138) ; AshenTaupe
            (154 154 138) ; AshenYellow
            (163 153 121) ; PaleTan
            (177 150 103) ; LightMustard
            (171 153 80)  ; LightTan
            (156 156 102) ; LightYellow
            (136 161 121) ; PaleMoss
            (139 158 144) ; AshenMint
            (140 157 157) ; AshenTurquoise
            (139 139 139) ; AshenGrey
            (109 121 126) ; RustSlate
            (97 124 124)  ; StaleTurquoise
            (116 121 107) ; RustLime
            (129 117 107) ; RustTaupe
            (147 109 118) ; RustFuchsia
            (136 111 136) ; RustViolet
            (159 100 141) ; StaleBerry
            (168 89 168)  ; WarmViolet
            (143 104 166) ; StaleLilac
            (111 111 191) ; WarmBlue
            (101 101 240) ; Blue
            (139 86 240)  ; Lavender
            (178 54 240)  ; Lilac
            (201 44 201)  ; Violet
            (245 82 245)  ; VividViolet
            (204 116 245) ; VividLilac
            (172 133 245) ; VividLavender
            (143 143 245) ; VividBlue
            (148 148 209) ; LightBlue
            (168 144 191) ; PaleLilac
            (185 134 209) ; LightLilac
            (193 135 177) ; PaleBerry
            (174 145 165) ; AshenBerry
            (179 145 145) ; AshenRed
            (216 181 181) ; CoolRed
            (229 178 160) ; StarkOrange
            (250 170 138) ; BrightOrange
            (250 172 113) ; BrightSepia
            (250 174 78)  ; BrightTaupe
            (236 180 59)  ; BrightMustard
            (217 188 59)  ; BrightTan
            (195 195 59)  ; BrightYellow
            (170 202 59)  ; BrightLime
            (133 209 59)  ; BrightMoss
            (59 217 59)   ; BrightGreen
            (127 208 127) ; StarkGreen
            (61 214 146)  ; BrightViridian
            (104 208 176) ; StarkViridian
            (151 201 163) ; CoolMint
            (154 199 183) ; CoolTeal
            (134 201 201) ; StarkTurquoise
            (65 208 208)  ; BrightTurquoise
            (66 206 228)  ; BrightSlate
            (79 203 249)  ; BrightAzure
            (130 196 249) ; StarkAzure
            (159 190 249) ; BrightCerulean
            (183 183 249) ; BrightBlue
            (197 183 226) ; StarkLavender
            (187 187 214) ; CoolBlue
            (202 184 202) ; WearyViolet
            (214 178 214) ; CoolViolet
            (217 174 237) ; BrightLilac
            (238 167 219) ; BrightMagenta
            (249 157 249) ; BrightViolet
            (229 111 197) ; LightBerry
            (247 104 151) ; VividFuchsia
            (216 127 152) ; LightFuchsia
            (218 129 129) ; LightRed
            (248 109 109) ; VividCherry
            (248 111 87)  ; VividRed
            (250 168 168) ; BrightRed
            (249 166 188) ; BrightFuchsia
            (252 215 252) ; LuminousViolet
            (237 222 237) ; ColdBerry
            (224 224 252) ; LuminousBlue
            (204 230 252) ; LuminousAzure
            (205 231 237) ; ColdSlate
            (169 237 252) ; LuminousSlate
            (157 196 206) ; CoolSlate
            (173 194 190) ; WearyTeal
            (182 182 182) ; CoolGrey
            (203 187 171) ; WearyMustard
            (218 183 152) ; CoolTaupe
            (218 184 128) ; StarkMustard
            (199 189 150) ; CoolTan
            (190 191 171) ; WearyYellow
            (181 195 150) ; CoolLime
            (168 200 127) ; StarkLime
            (193 193 127) ; StarkYellow
            (231 231 153) ; CrispYellow
            (214 237 120) ; CrispLime
            (181 246 72)  ; LuminousMoss
            (129 253 129) ; LuminousGreen
            (174 243 174) ; CrispGreen
            (210 235 180) ; ColdLime
            (187 238 213) ; ColdViridian
            (160 241 230) ; ColdTeal
            (126 248 217) ; CrispTeal
            (98 252 191)  ; LuminousViridian
            (79 249 249)  ; LuminousTurquoise
            (51 169 169)  ; VividTurquoise
            (108 163 163) ; LightTurquoise
            (52 167 189)  ; VividSlate
            (54 164 211)  ; VividAzure
            (111 160 186) ; LightAzure
            (129 156 187) ; PaleCerulean
            (109 151 245) ; VividCobalt
            (57 158 244)  ; VividCerulean
            (42 123 193)  ; Cerulean
            (40 127 166)  ; Azure
            (39 130 148)  ; Slate
            (37 131 132)  ; Turquoise
            (50 171 151)  ; VividTeal
            (105 166 139) ; LightViridian
            (48 173 128)  ; VividViridian
            (47 175 96)   ; VividMint
            (46 176 46)   ; VividGreen
            (117 167 79)  ; VividMoss
            (137 164 46)  ; VividLime
            (158 158 46)  ; VividYellow
            (189 147 46)  ; VividMustard
            (253 225 127) ; LuminousTan
            (248 224 174) ; CrispTan
            (238 225 200) ; ColdTan
            (252 221 197) ; LuminousTaupe
            (252 219 219) ; LuminousRed
            (226 226 226) ; White
            (170 192 214) ; CoolAzure
            (152 152 173) ; AshenBlue
            (117 117 144) ; RustBlue
            (100 121 147) ; StaleCerulean
            (48 112 240)  ; Cobalt
            (34 75 195)   ; DeepCobalt
            (55 55 232)   ; DeepBlue
            (25 25 172)   ; StrongBlue
            (20 46 138)   ; StrongCobalt
            (17 55 105)   ; StrongCerulean
            (15 59 84)    ; StrongAzure
            (14 61 73)    ; StrongSlate
            (13 62 62)    ; StrongTurquoise
            (12 64 43)    ; StrongViridian
            (3 33 3)      ; ShadowGreen
            (23 98 70)    ; DeepViridian
            (70 90 90)    ; SilkTurquoise
            (51 51 97)    ; DarkBlue
            (22 22 65)    ; NightBlue
            (9 9 97)      ; ShadowBlue
            (66 36 124)   ; StrongLavender
            (53 5 53)     ; ShadowViolet
            (34 23 43)    ; NightLilac
            (89 43 11)    ; StrongOrange
            (135 68 22)   ; DeepOrange
            (137 66 43)   ; HotOrange
            (233 233 72)  ; LuminousYellow
          )))

    ; Add the layer to the image
    (gimp-image-insert-layer img drawable 0 -1)

    ; Begin undo group
    (gimp-image-undo-group-start img)

    ; Loop through each pixel and set its color
    (let loop ((x 0))
      (if (< x 255)
          (let ((color (list-ref colors x)))
            ; Set foreground color
            (gimp-context-set-foreground color)
            ; Draw a single pixel
            (gimp-pencil drawable 2 (vector x 0 x 0))
            (loop (+ x 1)))))

    ; End undo group
    (gimp-image-undo-group-end img)

    ; Display the image
    (gimp-display-new img)))

; Register the script with GIMP
(script-fu-register
 "script-fu-palette-image"
 "Create Palette Image"
 "Creates a 255x1 image with each pixel set to a color from the provided palette"
 "Your Name"
 "Your Name"
 "2025"
 ""
 )

; Add to the Script-Fu menu
(script-fu-menu-register "script-fu-palette-image" "<Image>/File/Create")