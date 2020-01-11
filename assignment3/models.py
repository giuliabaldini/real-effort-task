from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import json
import os

author = 'Giulia Baldini, Maria Bigoni, Marco Fabbri'

doc = """
Effort task in which the players select the occurrences of a given number in a 17x17 matrix.
"""


class Constants(BaseConstants):
    name_in_url = 'assignment3'
    players_per_group = None

    # TODO: Change this to change the example
    example = [123, 231, 952, 864, 123, 791, 283, 123, 641, 820, 462, 123]

    # TODO: Add the correct numbers to find
    task_3_find = [835, 600, 915, 676, 775, 594, 351, 442, 234, 445, 276, 896, 368, 918, 307, 760, 582, 464, 161, 753,
                   186, 857, 824, 240, 305, 627, 123, 230, 582, 826, 592, 368, 762, 128, 165, 552, 523, 501, 717, 114,
                   367, 117, 195, 571, 474, 307, 388, 945, 952, 348]

    num_rounds = len(task_3_find)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            path = os.getcwd() + "/_static/global/matrix_ass3.json"
            jsonfile = open(path)
            self.session.vars['task_3_nums'] = json.loads(jsonfile.read())


class Group(BaseGroup):
    pass


def make_checkbox():
    return models.IntegerField(default=0, blank=True)


def return_fields(nums):
    start = 'cb_'
    forms = []
    for i in range(0, len(nums)):
        forms.append(start + str(i))
    return forms


class Player(BasePlayer):
    score = models.IntegerField(default=0)

    def compute_score(self):
        current_score = 0
        fields = {key: value for (key, value) in self.__dict__.items() if key[0:2] == 'cb'}

        current_constant = Constants.task_3_find[self.round_number - 1]
        for index, num in enumerate(self.session.vars['task_3_nums'][str(self.round_number)]):
            field_id = 'cb_' + str(index)
            if num == current_constant:
                if fields[field_id] == 1:
                    current_score += 1
            else:
                if fields[field_id] == 1:
                    current_score -= 1
        if 'player_score3' not in self.participant.vars:
            self.participant.vars['player_score3'] = current_score
        else:
            self.participant.vars['player_score3'] += current_score

    cb_0 = make_checkbox()
    cb_1 = make_checkbox()
    cb_2 = make_checkbox()
    cb_3 = make_checkbox()
    cb_4 = make_checkbox()
    cb_5 = make_checkbox()
    cb_6 = make_checkbox()
    cb_7 = make_checkbox()
    cb_8 = make_checkbox()
    cb_9 = make_checkbox()
    cb_10 = make_checkbox()
    cb_11 = make_checkbox()
    cb_12 = make_checkbox()
    cb_13 = make_checkbox()
    cb_14 = make_checkbox()
    cb_15 = make_checkbox()
    cb_16 = make_checkbox()
    cb_17 = make_checkbox()
    cb_18 = make_checkbox()
    cb_19 = make_checkbox()
    cb_20 = make_checkbox()
    cb_21 = make_checkbox()
    cb_22 = make_checkbox()
    cb_23 = make_checkbox()
    cb_24 = make_checkbox()
    cb_25 = make_checkbox()
    cb_26 = make_checkbox()
    cb_27 = make_checkbox()
    cb_28 = make_checkbox()
    cb_29 = make_checkbox()
    cb_30 = make_checkbox()
    cb_31 = make_checkbox()
    cb_32 = make_checkbox()
    cb_33 = make_checkbox()
    cb_34 = make_checkbox()
    cb_35 = make_checkbox()
    cb_36 = make_checkbox()
    cb_37 = make_checkbox()
    cb_38 = make_checkbox()
    cb_39 = make_checkbox()
    cb_40 = make_checkbox()
    cb_41 = make_checkbox()
    cb_42 = make_checkbox()
    cb_43 = make_checkbox()
    cb_44 = make_checkbox()
    cb_45 = make_checkbox()
    cb_46 = make_checkbox()
    cb_47 = make_checkbox()
    cb_48 = make_checkbox()
    cb_49 = make_checkbox()
    cb_50 = make_checkbox()
    cb_51 = make_checkbox()
    cb_52 = make_checkbox()
    cb_53 = make_checkbox()
    cb_54 = make_checkbox()
    cb_55 = make_checkbox()
    cb_56 = make_checkbox()
    cb_57 = make_checkbox()
    cb_58 = make_checkbox()
    cb_59 = make_checkbox()
    cb_60 = make_checkbox()
    cb_61 = make_checkbox()
    cb_62 = make_checkbox()
    cb_63 = make_checkbox()
    cb_64 = make_checkbox()
    cb_65 = make_checkbox()
    cb_66 = make_checkbox()
    cb_67 = make_checkbox()
    cb_68 = make_checkbox()
    cb_69 = make_checkbox()
    cb_70 = make_checkbox()
    cb_71 = make_checkbox()
    cb_72 = make_checkbox()
    cb_73 = make_checkbox()
    cb_74 = make_checkbox()
    cb_75 = make_checkbox()
    cb_76 = make_checkbox()
    cb_77 = make_checkbox()
    cb_78 = make_checkbox()
    cb_79 = make_checkbox()
    cb_80 = make_checkbox()
    cb_81 = make_checkbox()
    cb_82 = make_checkbox()
    cb_83 = make_checkbox()
    cb_84 = make_checkbox()
    cb_85 = make_checkbox()
    cb_86 = make_checkbox()
    cb_87 = make_checkbox()
    cb_88 = make_checkbox()
    cb_89 = make_checkbox()
    cb_90 = make_checkbox()
    cb_91 = make_checkbox()
    cb_92 = make_checkbox()
    cb_93 = make_checkbox()
    cb_94 = make_checkbox()
    cb_95 = make_checkbox()
    cb_96 = make_checkbox()
    cb_97 = make_checkbox()
    cb_98 = make_checkbox()
    cb_99 = make_checkbox()
    cb_100 = make_checkbox()
    cb_101 = make_checkbox()
    cb_102 = make_checkbox()
    cb_103 = make_checkbox()
    cb_104 = make_checkbox()
    cb_105 = make_checkbox()
    cb_106 = make_checkbox()
    cb_107 = make_checkbox()
    cb_108 = make_checkbox()
    cb_109 = make_checkbox()
    cb_110 = make_checkbox()
    cb_111 = make_checkbox()
    cb_112 = make_checkbox()
    cb_113 = make_checkbox()
    cb_114 = make_checkbox()
    cb_115 = make_checkbox()
    cb_116 = make_checkbox()
    cb_117 = make_checkbox()
    cb_118 = make_checkbox()
    cb_119 = make_checkbox()
    cb_120 = make_checkbox()
    cb_121 = make_checkbox()
    cb_122 = make_checkbox()
    cb_123 = make_checkbox()
    cb_124 = make_checkbox()
    cb_125 = make_checkbox()
    cb_126 = make_checkbox()
    cb_127 = make_checkbox()
    cb_128 = make_checkbox()
    cb_129 = make_checkbox()
    cb_130 = make_checkbox()
    cb_131 = make_checkbox()
    cb_132 = make_checkbox()
    cb_133 = make_checkbox()
    cb_134 = make_checkbox()
    cb_135 = make_checkbox()
    cb_136 = make_checkbox()
    cb_137 = make_checkbox()
    cb_138 = make_checkbox()
    cb_139 = make_checkbox()
    cb_140 = make_checkbox()
    cb_141 = make_checkbox()
    cb_142 = make_checkbox()
    cb_143 = make_checkbox()
    cb_144 = make_checkbox()
    cb_145 = make_checkbox()
    cb_146 = make_checkbox()
    cb_147 = make_checkbox()
    cb_148 = make_checkbox()
    cb_149 = make_checkbox()
    cb_150 = make_checkbox()
    cb_151 = make_checkbox()
    cb_152 = make_checkbox()
    cb_153 = make_checkbox()
    cb_154 = make_checkbox()
    cb_155 = make_checkbox()
    cb_156 = make_checkbox()
    cb_157 = make_checkbox()
    cb_158 = make_checkbox()
    cb_159 = make_checkbox()
    cb_160 = make_checkbox()
    cb_161 = make_checkbox()
    cb_162 = make_checkbox()
    cb_163 = make_checkbox()
    cb_164 = make_checkbox()
    cb_165 = make_checkbox()
    cb_166 = make_checkbox()
    cb_167 = make_checkbox()
    cb_168 = make_checkbox()
    cb_169 = make_checkbox()
    cb_170 = make_checkbox()
    cb_171 = make_checkbox()
    cb_172 = make_checkbox()
    cb_173 = make_checkbox()
    cb_174 = make_checkbox()
    cb_175 = make_checkbox()
    cb_176 = make_checkbox()
    cb_177 = make_checkbox()
    cb_178 = make_checkbox()
    cb_179 = make_checkbox()
    cb_180 = make_checkbox()
    cb_181 = make_checkbox()
    cb_182 = make_checkbox()
    cb_183 = make_checkbox()
    cb_184 = make_checkbox()
    cb_185 = make_checkbox()
    cb_186 = make_checkbox()
    cb_187 = make_checkbox()
    cb_188 = make_checkbox()
    cb_189 = make_checkbox()
    cb_190 = make_checkbox()
    cb_191 = make_checkbox()
    cb_192 = make_checkbox()
    cb_193 = make_checkbox()
    cb_194 = make_checkbox()
    cb_195 = make_checkbox()
    cb_196 = make_checkbox()
    cb_197 = make_checkbox()
    cb_198 = make_checkbox()
    cb_199 = make_checkbox()
    cb_200 = make_checkbox()
    cb_201 = make_checkbox()
    cb_202 = make_checkbox()
    cb_203 = make_checkbox()
    cb_204 = make_checkbox()
    cb_205 = make_checkbox()
    cb_206 = make_checkbox()
    cb_207 = make_checkbox()
    cb_208 = make_checkbox()
    cb_209 = make_checkbox()
    cb_210 = make_checkbox()
    cb_211 = make_checkbox()
    cb_212 = make_checkbox()
    cb_213 = make_checkbox()
    cb_214 = make_checkbox()
    cb_215 = make_checkbox()
    cb_216 = make_checkbox()
    cb_217 = make_checkbox()
    cb_218 = make_checkbox()
    cb_219 = make_checkbox()
    cb_220 = make_checkbox()
    cb_221 = make_checkbox()
    cb_222 = make_checkbox()
    cb_223 = make_checkbox()
    cb_224 = make_checkbox()
    cb_225 = make_checkbox()
    cb_226 = make_checkbox()
    cb_227 = make_checkbox()
    cb_228 = make_checkbox()
    cb_229 = make_checkbox()
    cb_230 = make_checkbox()
    cb_231 = make_checkbox()
    cb_232 = make_checkbox()
    cb_233 = make_checkbox()
    cb_234 = make_checkbox()
    cb_235 = make_checkbox()
    cb_236 = make_checkbox()
    cb_237 = make_checkbox()
    cb_238 = make_checkbox()
    cb_239 = make_checkbox()
    cb_240 = make_checkbox()
    cb_241 = make_checkbox()
    cb_242 = make_checkbox()
    cb_243 = make_checkbox()
    cb_244 = make_checkbox()
    cb_245 = make_checkbox()
    cb_246 = make_checkbox()
    cb_247 = make_checkbox()
    cb_248 = make_checkbox()
    cb_249 = make_checkbox()
    cb_250 = make_checkbox()
    cb_251 = make_checkbox()
    cb_252 = make_checkbox()
    cb_253 = make_checkbox()
    cb_254 = make_checkbox()
    cb_255 = make_checkbox()
    cb_256 = make_checkbox()
    cb_257 = make_checkbox()
    cb_258 = make_checkbox()
    cb_259 = make_checkbox()
    cb_260 = make_checkbox()
    cb_261 = make_checkbox()
    cb_262 = make_checkbox()
    cb_263 = make_checkbox()
    cb_264 = make_checkbox()
    cb_265 = make_checkbox()
    cb_266 = make_checkbox()
    cb_267 = make_checkbox()
    cb_268 = make_checkbox()
    cb_269 = make_checkbox()
    cb_270 = make_checkbox()
    cb_271 = make_checkbox()
    cb_272 = make_checkbox()
    cb_273 = make_checkbox()
    cb_274 = make_checkbox()
    cb_275 = make_checkbox()
    cb_276 = make_checkbox()
    cb_277 = make_checkbox()
    cb_278 = make_checkbox()
    cb_279 = make_checkbox()
    cb_280 = make_checkbox()
    cb_281 = make_checkbox()
    cb_282 = make_checkbox()
    cb_283 = make_checkbox()
    cb_284 = make_checkbox()
    cb_285 = make_checkbox()
    cb_286 = make_checkbox()
    cb_287 = make_checkbox()
    cb_288 = make_checkbox()

    # TODO: Add as many as the number of numbers per task
