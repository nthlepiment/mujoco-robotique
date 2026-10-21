import time
import numpy as np
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("mujoco_menagerie/franka_emika_panda/scene.xml")
data = mujoco.MjData(model)

print("Nombre d'articulations :", model.nq)
print("Nombre de moteurs :", model.nu)

with mujoco.viewer.launch_passive(model, data) as viewer:
    t0 = time.time()
    while viewer.is_running():
        t = time.time() - t0
        # On fait osciller le premier axe du bras
        data.ctrl[0] = 0.8 * np.sin(t)
        data.ctrl[1] = 0.5 * np.sin(2 * t)
        data.ctrl[3] = -1.5 + 0.5 * np.sin(t)
        mujoco.mj_step(model, data)
        print(f"consigne={data.ctrl[0]:.2f}  position réelle={data.qpos[0]:.2f}", end="\r")
        viewer.sync()
        time.sleep(model.opt.timestep)