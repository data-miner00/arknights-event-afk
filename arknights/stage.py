from enum import Enum
from arknights.week import DayOfWeek


class Stage(Enum):
    def __str__(self) -> str:
        return str(self.value)

    CA5 = "ca5"
    SK5 = "sk5"
    CE6 = "ce6"
    LS6 = "ls6"
    PRA1 = "pra1"
    PRA2 = "pra2"
    PRB1 = "prb1"
    PRB2 = "prb2"
    PRC1 = "prc1"
    PRC2 = "prc2"
    PRD1 = "prd1"
    PRD2 = "prd2"


__stage_list = [
    Stage.CA5,
    Stage.SK5,
    Stage.CE6,
    Stage.LS6,
    Stage.PRA1,
    Stage.PRA2,
    Stage.PRB1,
    Stage.PRB2,
    Stage.PRC1,
    Stage.PRC2,
    Stage.PRD1,
    Stage.PRD2,
]

stage_list = list(map(lambda x: x.value, __stage_list))


pra_days_of_week = [
    DayOfWeek.MONDAY,
    DayOfWeek.THURSDAY,
    DayOfWeek.FRIDAY,
    DayOfWeek.SUNDAY,
]
prb_days_of_week = [
    DayOfWeek.MONDAY,
    DayOfWeek.TUESDAY,
    DayOfWeek.FRIDAY,
    DayOfWeek.SATURDAY,
]
prc_days_of_week = [
    DayOfWeek.WEDNESDAY,
    DayOfWeek.THURSDAY,
    DayOfWeek.SATURDAY,
    DayOfWeek.SUNDAY,
]
prd_days_of_week = [
    DayOfWeek.TUESDAY,
    DayOfWeek.WEDNESDAY,
    DayOfWeek.SATURDAY,
    DayOfWeek.SUNDAY,
]

stage_available_day_of_week = {
    Stage.CE6: [
        DayOfWeek.TUESDAY,
        DayOfWeek.THURSDAY,
        DayOfWeek.SATURDAY,
        DayOfWeek.SUNDAY,
    ],
    Stage.LS6: [day for day in DayOfWeek],
    Stage.SK5: [
        DayOfWeek.MONDAY,
        DayOfWeek.WEDNESDAY,
        DayOfWeek.FRIDAY,
        DayOfWeek.SATURDAY,
    ],
    Stage.CA5: [
        DayOfWeek.TUESDAY,
        DayOfWeek.WEDNESDAY,
        DayOfWeek.FRIDAY,
        DayOfWeek.SUNDAY,
    ],
    Stage.PRA1: pra_days_of_week,
    Stage.PRA2: pra_days_of_week,
    Stage.PRB1: prb_days_of_week,
    Stage.PRB2: prb_days_of_week,
    Stage.PRC1: prc_days_of_week,
    Stage.PRC2: prc_days_of_week,
    Stage.PRD1: prd_days_of_week,
    Stage.PRD2: prd_days_of_week,
}

stage_info = {
    Stage.CE6: "The stage to obtain Lungmen currency",
    Stage.LS6: "The stage to obtain Exp books",
    Stage.SK5: "The stage to obtain carbon",
    Stage.CA5: "The stage to obtain talent books",
    Stage.PRA1: "The stage to obtain first-tier ascention material for Medics and Defender",
    Stage.PRA2: "The stage to obtain second-tier ascention material for Medics and Defender",
    Stage.PRB1: "The stage to obtain first-tier ascention material for Sniper and Caster",
    Stage.PRB2: "The stage to obtain second-tier ascention material for Sniper and Caster",
    Stage.PRC1: "The stage to obtain first-tier ascention material for Vanguard and Supporter",
    Stage.PRC2: "The stage to obtain second-tier ascention material for Vanguard and Supporter",
    Stage.PRD1: "The stage to obtain first-tier ascention material for Guard and Specialist",
    Stage.PRD2: "The stage to obtain second-tier ascention material for Guard and Specialist",
}


def show_info(stage):
    def show_individual_info(stage):
        enum_stage = getattr(Stage, stage.upper())
        stringified_stage_weeks = list(
            map(str, stage_available_day_of_week[enum_stage])
        )
        print(
            f"{stage} - {stage_info[enum_stage]}, available on {', '.join(stringified_stage_weeks)}"
        )

    print("Stage info")
    print("----------")
    if stage == "all":
        for stg in stage_list:
            show_individual_info(stg)
    else:
        show_individual_info(stage)
