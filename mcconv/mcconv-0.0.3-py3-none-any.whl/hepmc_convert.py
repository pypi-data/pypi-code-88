import logging
import time

from pyHepMC3 import HepMC3 as hm

from mcconv import detect_mc_type
from .generic_reader import GenericTextReader, UnparsedTextEvent
from .formats.pythia6 import parse_lund_particles, LundReader, parse_lund_particle_tokens
from .file_types import McFileTypes

logger = logging.getLogger("mcconv.hepmc_convert")


def hepmc_write(input_file, output_file, input_type, output_type, progress_func=None, nskip=0, nprocess=0):
    # hepmc 2 or 3 writer

    if output_type == 2 or output_type == "2" or (isinstance(output_type, str) and output_type.lower() == "hepmc2"):
        writer = hm.WriterAsciiHepMC2(output_file)
    else:
        writer = hm.WriterAscii(output_file)

    if not input_type or input_type == McFileTypes.UNKNOWN:
        logger.debug("Input file type is not given or UNKNOWN. Trying autodetect")
        input_type = detect_mc_type(input_file)

    if input_type == McFileTypes.UNKNOWN:
        raise ValueError("File format is UNKNOWN")

    reader = LundReader()
    reader.open(input_file)

    # This is basically the same as with statement. But HepMcWriter doesn't implement __enter__() etc.
    evt = hm.GenEvent(hm.Units.GEV, hm.Units.MM)
    start_time = time.time()
    try:
        for evt_index, unparsed_evt in enumerate(reader.unparsed_events()):

            # Should we skip the event?
            if nskip > evt_index:
                if progress_func:
                    progress_func(evt_index, evt, "skipped")
                continue
            simple_convert_lund_event(evt, unparsed_evt)
            if progress_func:
                progress_func(evt_index, evt, "processed")
            writer.write_event(evt)
            evt.clear()

            # Should we break?
            if nprocess and nprocess + nskip == evt_index + 1:
                break
    finally:
        writer.close()
        reader.close()
        evt.clear()
        logger.info(f"Time for the conversion = {time.time() - start_time} sec")


def simple_convert_lund_event(hepmc_evt, unparsed_event):
    assert isinstance(unparsed_event, UnparsedTextEvent)

    hepmc_evt.add_attribute("start_line_index", hm.IntAttribute(unparsed_event.start_line_index))

    v1 = hm.GenVertex()
    hepmc_evt.add_vertex(v1)

    #particles = parse_lund_particles(unparsed_event)
    for particle_line in unparsed_event.particle_tokens:
        particle = parse_lund_particle_tokens(particle_line)
        if particle.status != 1:
            continue
        hm_particle = hm.GenParticle(hm.FourVector(particle.px, particle.py, particle.pz, particle.energy), particle.pdg, particle.status)

        hepmc_evt.add_particle(hm_particle)

    return hepmc_evt


def _add_gemc_lund_particle_attributes(hm_particle, gemc_particle):
    hm_particle.add_attribute("life_time", hm.DoubleAttribute(gemc_particle.lifetime))


    #evt.set_event_number(1)
    #evt.add_attribute("signal_process_id", hm.IntAttribute(20))

